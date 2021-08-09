from flask import Flask, request, Response
import psycopg2

from model import package
import db_credentials
import db_operations
import constants

app = Flask(__name__)


@app.route('/example', methods=['POST'])
def upload_example():
    if not request.json:
        return Response(response="{'error': 'Missing package'}", status=400)
    try:
        pack = package.Package(constants.PayloadTypes.temp_and_hum.name, **request.json['package']) # ToDo
        credentials = db_credentials.DbCredentials(**request.json['Db_connection'])
    except TypeError as e:
        return Response(response="malformed http body", status=400)

    # Establish connection
    try:
        session_instance = db_operations.DbSession(credentials, constants.TEMPERATURE_DATABASE_HOST, constants.TEMPERATURE_DATABASE)    # ToDo
    except (Exception, psycopg2.Error) as error:
        print("Database authentication failed")
        return Response(response="Database authentication failed", status=401)

    try:
        session_instance.upload_package(pack)
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert records with error:", error)
        return Response(response=f"Failed to insert records with error: {error}", status=400)
    return Response(response="Package stored successfully", status=200)


@app.route('/temp-hum', methods=['POST'])
def upload_temp_and_humidity():
    if not request.json:
        return Response(response="{'error': 'Missing package'}", status=400)
    try:
        pack = package.Package(constants.PayloadTypes.temp_and_hum.name, **request.json['package'])
        credentials = db_credentials.DbCredentials(**request.json['Db_connection'])
    except TypeError as e:
        return Response(response="malformed http body", status=400)

    # Establish connection
    try:
        session_instance = db_operations.DbSession(credentials, constants.TEMPERATURE_DATABASE_HOST, constants.TEMPERATURE_DATABASE)
    except (Exception, psycopg2.Error) as error:
        print("Database authentication failed")
        return Response(response="Database authentication failed", status=401)

    try:
        session_instance.upload_package(pack)
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert records with error:", error)
        return Response(response=f"Failed to insert records with error: {error}", status=400)
    return Response(response="Package stored successfully", status=200)


@app.route('/seismic-data', methods=['POST'])
def upload_seismic_package():
    if not request.json:
        return Response(response="{Missing package}", status=400)

    try:
        pack = package.Package(constants.PayloadTypes.seismic.name, **request.json['package'])
        credentials = db_credentials.DbCredentials(**request.json['Db_connection'])
    except TypeError as e:
        return Response(response="Http body malformed", status=400)

    # Establish connection
    try:
        session_instance = db_operations.DbSession(credentials, constants.SEISMIC_DATABASE_HOST, constants.SEISMIC_DATABASE)
    except (Exception, psycopg2.Error) as error:
        print("Database authentication failed")
        return Response(response="Database authentication failed", status=401)

    try:
        session_instance.upload_package(pack)
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert records with error:", error)
        return Response(response=f"Failed to insert records with error: {error}", status=400)
    return Response(response="Package stored successfully", status=200)


@app.route('/ultrasound', methods=['POST'])
def upload_ultrasound_package():
    if not request.json:
        return Response(response="{Missing package}", status=400)

    try:
        pack = package.Package(constants.PayloadTypes.ultrasound.name, **request.json['package'])
        credentials = db_credentials.DbCredentials(**request.json['Db_connection'])
    except TypeError as e:
        return Response(response="Http body malformed", status=400)

    # Establish connection
    try:
        session_instance = db_operations.DbSession(credentials, constants.ULTRASOUND_DATABASE_HOST, constants.ULTRASOUND_DATABASE)
    except (Exception, psycopg2.Error) as error:
        print("Database authentication failed")
        return Response(response="Database authentication failed", status=401)

    try:
        session_instance.upload_package(pack)
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert records with error:", error)
        return Response(response=f"Failed to insert records with error: {error}", status=400)
    return Response(response="Package stored successfully", status=200)


@app.route('/')
def index():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)
