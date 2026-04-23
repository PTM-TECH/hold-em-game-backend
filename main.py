from flask import Flask, jsonify, Blueprint
from prisma import Prisma
from dotenv import load_dotenv
import asyncio
from app import create_app


app = Flask(__name__)

#define the blueprint
student_bp = Blueprint("student_bp", __name__)

@student_bp.route("/single", methods=["GET"])
async def sing_student():
    return "single student"
    # prisma = Prisma()
    # try:
    #     await prisma.connect()

    #     student =  await prisma.student.find_first()
    #     student_dict = student.model_dump()
    #     return jsonify(student_dict),200
    # finally:
    #     prisma.disconnect()
@student_bp.route("/add", methods =["POST"])
async def add():
    return "adding student"

@student_bp.route("/delete", methods=["DELETE"])
async def delete_student():
    return "delete student"

@student_bp.route("/list-all", methods=["GET"])
async def list_all():
    return "list student"


if __name__ == "__main__":
    # app.register_blueprint(student_bp, url_prefix="/student")
    app=create_app()
    app.run(debug=True, port=5001)