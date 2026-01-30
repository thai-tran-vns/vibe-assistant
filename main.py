import asyncio
import signal
import sys
from loguru import logger
import aioconsole

# Configure logging
logger.remove()
logger.add("app.log", level="DEBUG", rotation="1 MB")
logger.add(sys.stderr, level="WARNING")

async def user_loop():
    """Handles user input asynchronously."""
    logger.info("User loop started")
    while True:
        try:
            # Use aioconsole for non-blocking input
            user_input = await aioconsole.ainput("You: ")
            print(f"Echo: {user_input}")
            logger.info(f"User input: {user_input}")
        except asyncio.CancelledError:
            logger.info("User loop cancelled")
            raise
        except Exception as e:
            logger.error(f"Error in user loop: {repr(e)}")
            # Prevent tight loop on error
            await asyncio.sleep(1)

async def agent_loop():
    """Simulates background agent work."""
    logger.info("Agent loop started")
    while True:
        try:
            logger.info("Agent heartbeat...")
            await asyncio.sleep(5)
        except asyncio.CancelledError:
            logger.info("Agent loop cancelled")
            raise
        except Exception as e:
            logger.error(f"Error in agent_loop: {repr(e)}")
            await asyncio.sleep(1)

async def main():
    """Main entry point with graceful shutdown."""
    loop = asyncio.get_running_loop()
    stop_event = asyncio.Event()

    def signal_handler():
        logger.warning("Shutdown signal received")
        stop_event.set()

    # Register signal handlers
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, signal_handler)

    logger.info("Application started")

    # Start background tasks
    user_task = asyncio.create_task(user_loop())
    agent_task = asyncio.create_task(agent_loop())

    # Wait for shutdown signal
    await stop_event.wait()

    logger.info("Shutdown initiated")

    # Cancel all running tasks except current
    current_task = asyncio.current_task()
    tasks = [t for t in asyncio.all_tasks() if t is not current_task]

    for task in tasks:
        task.cancel()

    # Wait for tasks to complete/cancel
    results = await asyncio.gather(*tasks, return_exceptions=True)

    for result in results:
        if isinstance(result, Exception) and not isinstance(result, asyncio.CancelledError):
            logger.error(f"Task failed during shutdown: {result}")

    logger.info("Shutdown complete")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        # Fallback for environments where signal handlers might be tricky
        pass
