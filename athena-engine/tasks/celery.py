from celery import Celery

app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=["tasks.scoring_tasks"],
)

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == "__main__":
    app.start()
