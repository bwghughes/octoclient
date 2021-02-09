import os
import solax
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler

async def tick():
    print("Polling inverter for data....")
    r = await solax.real_time_api('5.8.8.8')
    inverter_data = await r.get_data()
    print(inverter_data)
    return await r.get_data()


scheduler = AsyncIOScheduler()
scheduler.add_job(tick, 'interval', seconds=10)
scheduler.start()
print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

# Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
try:
    asyncio.get_event_loop().run_forever()
except (KeyboardInterrupt, SystemExit):
    pass 
