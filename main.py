import os
import solax
import typer
import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from loguru import logger as l
from tortoise import Tortoise, run_async

from models import SolaxInverter

app = typer.Typer()


async def process_fields(data):
    r = {}
    for k, v in data.items():
        r[k.lower().replace(' ', '_').replace("'", "").replace('-', '_')] = v
    l.info(r)
    return r


async def tick():
    l.info("Polling inverter for data....")
    r = await solax.real_time_api('5.8.8.8')
    inverter_data = await r.get_data()
    l.info("Logging to db...")
    inverter_response = await r.get_data()
    new_dict = await process_fields(inverter_response.data)
    return await writeDB(new_dict)
    
    
async def writeDB(row):
    l.info(f"Creating new record with: {row}...")
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['models']}
    )
    i = SolaxInverter(**row)
    result = await i.save()
    return result
    

@app.command()
def poll(interval: int=10):
    scheduler = AsyncIOScheduler()
    scheduler.add_job(tick, 'interval', seconds=interval)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    
    # Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass 
        
    
@app.command()
def seed():
    async def init():
        # Here we create a SQLite DB using file "db.sqlite3"
        #  also specify the app name of "models"
        #  which contain models from "app.models"
        await Tortoise.init(
            db_url='sqlite://db.sqlite3',
            modules={'models': ['models']}
        )
        # Generate the schema
        await Tortoise.generate_schemas()
    
    # run_async is a helper function to run simple async Tortoise scripts.
    run_async(init())
    
if __name__ == "__main__":
    app()


