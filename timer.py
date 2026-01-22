import azure.functions as func
import logging
from datetime import datetime
from task import tasks

def register_timer(app: func.FunctionApp):
    @app.schedule(
        schedule="0 0 * * * *",
        arg_name="timer",
        run_on_startup=False,
        use_monitor=True
    )
    def log_task_stats(timer: func.TimerRequest) -> None:
        total = len(tasks)
        completed = sum(1 for t in tasks if t["completed"])
        in_progress = total - completed

        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

        logging.info(
            f"[{timestamp}] Stats: {total} tâches totales, "
            f"{completed} complétée(s), {in_progress} en cours"
        )