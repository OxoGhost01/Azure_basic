import azure.functions as func
import logging
import json

tasks = [
            { "id": 1, "title": "Apprendre Azure Functions", "completed": False },
            { "id": 2, "title": "Déployer en production", "completed": False }
        ]

def register_routes(app: func.FunctionApp):
    
    @app.route(route="tasks", methods=["GET"])
    def get_tasks(req: func.HttpRequest) -> func.HttpResponse:
        logging.info('GET /api/tasks called')

        return(
            func.HttpResponse(
                body = json.dumps(tasks),
                status_code = 200
            )
        )
    
    @app.route(route="tasks", methods=["POST"])
    def add_task(req: func.HttpRequest) -> func.HttpResponse:
        logging.info('POST /api/tasks called')
        body = req.get_json()

        title = body.get("title")

        id = max(task["id"] for task in tasks) + 1
        tasks.append({
            "id": id,
            "title": title,
            "completed": False
        })


        return(
            func.HttpResponse(
                body = json.dumps(tasks),
                status_code = 201
            )
        )
    
    @app.route(route="tasks/{id}/completed", methods=["PUT"])
    def get_task(req: func.HttpRequest) -> func.HttpResponse:
        logging.info('GET /api/tasks/{id}/completed called')

        id = int(req.route_params.get("id"))
        id = int(id)

        for task in tasks:
            if task["id"] == id:
                task["completed"] = True

        return(
            func.HttpResponse(
                body = json.dumps(tasks),
                status_code = 201
            )
        )