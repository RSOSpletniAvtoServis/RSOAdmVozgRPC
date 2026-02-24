from concurrent import futures
import grpc

import admvozgrpc_pb2
import admvozgrpc_pb2_grpc

import mysql.connector
from mysql.connector import pooling
import time

from grpc_health.v1 import health, health_pb2, health_pb2_grpc

for i in range(5):
    try:
        pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host="127.0.0.1", #34.44.150.229", #127.0.0.1",
            user="zan",
            password=">tnitm&+NqgoA=q6",
            database="RSOAdminVozila",
            autocommit=True
        )
        break
    except Exception as e:
        print("Error: ",e)
        print(f"DB connection failed, retrying... ({i+1}/5)")
        time.sleep(5)
else:
    raise RuntimeError("Could not connect to the database after 5 attempts")


# -------------------------
# Service Implementation
# -------------------------

class AdminService(admvozgrpc_pb2_grpc.AdminServiceServicer):

    # -------------------------
    # 1️ IzbraniKraji
    # -------------------------
    def IzbraniKraji(self, request, context):
        response = admvozgrpc_pb2.IzbraniKrajiResponse()
        
        # start implementation
        ids_string = "("
        idmiddle = ",".join(str(i) for i in request.ids)
        full_string = "(" + idmiddle + ")"
        print(ids_string)
        print(idmiddle)
        print(full_string)
        
        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = "SELECT IDKraj, NazivKraja FROM Kraj WHERE IDKraj IN " + full_string
                    cursor.execute(sql)
                    rows = cursor.fetchall()

            for row in rows:
                kraj = admvozgrpc_pb2.Kraj(
                    IDKraj=int(row[0]),
                    NazivKraja=row[1],
                )
                response.kraji.append(kraj)
            return response
        except Exception as e:
            print("DB error:", e)
            context.abort(grpc.StatusCode.NOT_FOUND, "Error: "+e)
            return response    
        # end implementation
        return response


    # -------------------------
    # 2️ IzbraneStoritve
    # -------------------------
    def IzbraneStoritve(self, request, context):
        response = admvozgrpc_pb2.IzbraneStoritveResponse()
        
        # start implementation
        ids_string = "("
        idmiddle = ",".join(str(i) for i in request.ids)
        full_string = "(" + idmiddle + ")"
        print(ids_string)
        print(idmiddle)
        print(full_string)
        
        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = "SELECT IDStoritev, NazivStoritve FROM Storitev WHERE IDStoritev IN " + full_string
                    cursor.execute(sql)
                    rows = cursor.fetchall()

            for row in rows:
                storitev = admvozgrpc_pb2.Storitev(
                    IDStoritev=int(row[0]),
                    NazivStoritve=row[1],
                )
                response.storitve.append(storitev)
            return response
        except Exception as e:
            print("DB error:", e)
            context.abort(grpc.StatusCode.NOT_FOUND, "Error: "+e)
            return response    
        # end implementation
        return response
    # implementacija end



    # -------------------------
    # 3️ IzbraniStatusi
    # -------------------------
    def IzbraniStatusi(self, request, context):
        response = admvozgrpc_pb2.IzbraniStatusiResponse()
        
        # start implementation
        ids_string = "("
        idmiddle = ",".join(str(i) for i in request.ids)
        full_string = "(" + idmiddle + ")"
        print(ids_string)
        print(idmiddle)
        print(full_string)
        
        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = "SELECT IDStatus, NazivStatusa FROM Status WHERE IDStatus IN " + full_string
                    cursor.execute(sql)
                    rows = cursor.fetchall()

            for row in rows:
                status = admvozgrpc_pb2.Status(
                    IDStatus=int(row[0]),
                    NazivStatusa=row[1],
                )
                response.statusi.append(status)
            return response
        except Exception as e:
            print("DB error:", e)
            context.abort(grpc.StatusCode.NOT_FOUND, "Error: "+e)
            return response    
        # end implementation
        return response        
        


    # -------------------------
    # 4 IzbranaVozila
    # -------------------------
    def IzbranaVozila(self, request, context):
        response = admvozgrpc_pb2.IzbranaVozilaResponse()
        # implementacija zacetek     
        ids_string = "("
        idmiddle = ",".join("'"+str(i)+"'" for i in request.stsas)
        full_string = "(" + idmiddle + ")"
        print(ids_string)
        print(idmiddle)
        print(full_string)
        
        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = "SELECT v.StevilkaSasije, v.IDZnamka, v.IDModel, z.NazivZnamke, m.NazivModel  FROM Vozilo v, Znamka z, Model m WHERE v.IDZnamka = z.IDZnamka AND v.IDModel = m.IDModel AND v.IDUporabnik = %s AND v.StevilkaSasije IN " + full_string
                    cursor.execute(sql,(request.iduporabnik,))
                    rows = cursor.fetchall()
                    for row in rows:
                        vozilo = admvozgrpc_pb2.Vozilo(
                            StevilkaSasije=row[0],
                            IDZnamka=row[1],
                            IDModel=row[2],
                            NazivZnamke=row[3],
                            NazivModel=row[4],
                        )
                        response.vozila.append(vozilo)
                    return response
        except Exception as e:
            print("DB error:", e)
            context.abort(grpc.StatusCode.NOT_FOUND, "Error: "+e)
            return response
        # implementacija end
        return response    


    # -------------------------
    # 5 IzbranaVozila1
    # -------------------------
    def IzbranaVozila1(self, request, context):
        response = admvozgrpc_pb2.IzbranaVozila1Response()
        # implementacija zacetek     
        ids_string = "("
        idmiddle = ",".join("'"+str(i)+"'" for i in request.stsas)
        full_string = "(" + idmiddle + ")"
        print(ids_string)
        print(idmiddle)
        print(full_string)
        
        try:
            with pool.get_connection() as conn:
                with conn.cursor() as cursor:
                    sql = "SELECT v.StevilkaSasije, v.IDZnamka, v.IDModel, z.NazivZnamke, m.NazivModel  FROM Vozilo v, Znamka z, Model m WHERE v.IDZnamka = z.IDZnamka AND v.IDModel = m.IDModel AND v.StevilkaSasije IN " + full_string
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    for row in rows:
                        vozilo = admvozgrpc_pb2.Vozilo(
                            StevilkaSasije=row[0],
                            IDZnamka=row[1],
                            IDModel=row[2],
                            NazivZnamke=row[3],
                            NazivModel=row[4],
                        )
                        response.vozila.append(vozilo)
                    return response
        except Exception as e:
            print("DB error:", e)
            context.abort(grpc.StatusCode.NOT_FOUND, "Error: "+e)
            return response
        # implementacija end
        return response         


# -------------------------
# Server Setup
# -------------------------

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    admvozgrpc_pb2_grpc.add_AdminServiceServicer_to_server(AdminService(), server)
    
    # Create health servicer
    health_servicer = health.HealthServicer()

    # Register health service
    health_pb2_grpc.add_HealthServicer_to_server(
        health_servicer, server
    )
    
     # Mark service as NOT_SERVING initially
    health_servicer.set('', health_pb2.HealthCheckResponse.NOT_SERVING)
    
    server.add_insecure_port('[::]:50051')
    server.start()


    # Simulate startup work
    time.sleep(5)

    # Mark as ready
    health_servicer.set('', health_pb2.HealthCheckResponse.SERVING)
    
    print("AdminService gRPC server running on port 50051...")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()