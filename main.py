import asyncio
import sys
import os
from loguru import logger
import aioconsole

# Ensure logs directory exists
if not os.path.exists("logs"):
    os.makedirs("logs")

def setup_logging():
    """Configures the application logging."""
    logger.remove()
    logger.add("logs/app.log", level="DEBUG", rotation="1 MB")

async def user_loop():
    """Handles user input asynchronously."""
    logger.info("User loop started")
    while True:
        try:
            # Use aioconsole for non-blocking input
            user_input = await aioconsole.ainput(">>> ")
            
            if user_input.strip().lower() in ["exit", "quit"]:
                print("Exiting...")
                logger.info("User requested exit")
                break
            
            # Echo input for now
            print(f"Echo: {user_input}")
            logger.info(f"User input: {user_input}")
            
        except asyncio.CancelledError:
            logger.info("User loop cancelled")
            raise
        except Exception as e:
            logger.error(f"Error in user loop: {repr(e)}")
            # Prevent tight loop on error
            await asyncio.sleep(1)

async def supervisor_loop():
    """Background supervisor loop."""
    logger.info("Supervisor loop started")
    while True:
        try:
            logger.debug("Supervisor heartbeat...")
            await asyncio.sleep(1) # Sleep for a short interval
        except asyncio.CancelledError:
            logger.info("Supervisor loop cancelled")
            raise
        except Exception as e:
            logger.error(f"Error in supervisor_loop: {repr(e)}")
            await asyncio.sleep(1)

async def main():
    """Main execution entry point."""
    setup_logging()
    logger.info("Application started")
    
    # Create tasks
    supervisor_task = asyncio.create_task(supervisor_loop())
    user_task = asyncio.create_task(user_loop())
    
    tasks = [supervisor_task, user_task]
    
    try:
        # Wait for the user loop to complete or a signal
        # We await user_task primarily because if the user types 'exit', we want to stop.
        # However, asyncio.gather is requested/suggested. 
        # If we use gather, we need to handle the fact that supervisor never ends.
        
        # Using wait to handle 'exit' command from user_loop naturally
        done, pending = await asyncio.wait(
            [user_task], 
            return_when=asyncio.FIRST_COMPLETED
        )
        
    except asyncio.CancelledError:
        logger.info("Main task cancelled")
    except KeyboardInterrupt:
        logger.info("KeyboardInterrupt received")
    finally:
        logger.info("Shutting down...")
        
        # Cancel all pending tasks (this includes supervisor_loop if user_loop finished,
        # or both if KeyboardInterrupt happened)
        for task in tasks:
            if not task.done():
                task.cancel()
        
        # Wait for cancellation to propagate
        await asyncio.gather(*tasks, return_exceptions=True)
        logger.info("Shutdown complete")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully if it happens outside the async loop (e.g. startup)
        pass