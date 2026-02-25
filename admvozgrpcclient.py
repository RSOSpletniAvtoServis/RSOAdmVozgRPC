import grpc

import admvozgrpc_pb2
import admvozgrpc_pb2_grpc


def get_izbraniKraji():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = admvozgrpc_pb2_grpc.AdminServiceStub(channel)

        kraji_response = stub.IzbraniKraji(
            admvozgrpc_pb2.GetIzbraniKrajiRequest(
                ids=[],
                uniqueid="123"
            )
        )

        print("\nKraji:")
        for kraj in kraji_response.kraji:
            print(kraj.IDKraj, kraj.NazivKraja)

# -------------------------
# 2️ Izbrane storitve
# -------------------------
def get_izbraneStoritve():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = admvozgrpc_pb2_grpc.AdminServiceStub(channel)

        storitve_response = stub.IzbraneStoritve(
            admvozgrpc_pb2.GetIzbraneStoritveRequest(
                ids=[7, 8, 9],
                uniqueid="123"
            )
        )

        print("\nStoritve:")
        for storitev in storitve_response.storitve:
            print(storitev.IDStoritev, storitev.NazivStoritve)

# -------------------------
# 3 Izbrani statusi
# -------------------------   

def get_izbraniStatusi():   
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = admvozgrpc_pb2_grpc.AdminServiceStub(channel)

        status_response = stub.IzbraniStatusi(
            admvozgrpc_pb2.GetIzbraniStatusiRequest(
                ids=[1, 2, 3],
                uniqueid="123"
            )
        )

        print("\nStatusi:")
        for status in status_response.statusi:
            print(status.IDStatus, status.NazivStatusa)

# -------------------------
# 4 Izbrana vozila
# -------------------------   

def get_izbranaVozila():   
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = admvozgrpc_pb2_grpc.AdminServiceStub(channel)

        vozilo_response = stub.IzbranaVozila(
            admvozgrpc_pb2.GetIzbranaVozilaRequest(
                stsas=["bmwdkdeofw02","dwjdjwoa","euiw2938221"],
                iduporabnik=5,
                uniqueid="123"
            )
        )

        print("\nVozila:")
        for vozilo in vozilo_response.vozila:
            print(vozilo.StevilkaSasije, vozilo.IDZnamka, vozilo.IDModel, vozilo.NazivZnamke, vozilo.NazivModel)
            
            
# -------------------------
# 5 Izbrana vozila 1
# -------------------------   

def get_izbranaVozila1():   
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = admvozgrpc_pb2_grpc.AdminServiceStub(channel)

        vozilo_response = stub.IzbranaVozila1(
            admvozgrpc_pb2.GetIzbranaVozila1Request(
                stsas=[],
                #stsas=["bmwdkdeofw02","dwjdjwoa","euiw2938221"],
                uniqueid="123"
            )
        )

        print("\nVozila1:")
        for vozilo in vozilo_response.vozila:
            print(vozilo.StevilkaSasije, vozilo.IDZnamka, vozilo.IDModel, vozilo.NazivZnamke, vozilo.NazivModel)



def run():
    get_izbraniKraji()
    get_izbraneStoritve()
    get_izbraniStatusi()
    get_izbranaVozila()
    get_izbranaVozila1()






if __name__ == "__main__":
    run()