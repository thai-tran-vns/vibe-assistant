import asyncio
import sys
from loguru import logger
import aioconsole

# 1. Logging Configuration
logger.remove()
logger.add("app.log", level="DEBUG")
logger.add(sys.stderr, level="WARNING")

async def user_loop():
    logger.info("User loop started.")
    while True:
        try:
            user_input = await aioconsole.ainput("You: ")
            logger.info(f"User input: {user_input}")
            print(f"Echo: {user_input}")
        except EOFError:
            logger.info("User input stream closed (EOF).")
            break
        except asyncio.CancelledError:
            break

async def agent_loop():
    logger.info("Agent loop started.")
    try:
        while True:
            logger.info("Agent heartbeat...")
            await asyncio.sleep(5)
    except asyncio.CancelledError:
        pass

async def main():
    await asyncio.gather(user_loop(), agent_loop())

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass