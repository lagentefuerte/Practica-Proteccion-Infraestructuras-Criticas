def read_coil(conn, uid, start_address):
        packet = random.randbytes(2)   # id de transaccion (2 bytes) (aleatorio)
        packet += b'\x00\x00'     # id de protocolo (2 bytes) (siempre 0)
        packet += b'\x00\x06'             # longitud (2 bytes) (siempre 6 bytes en estas funciones)
        packet += p8(uid)                 # id de unidad (1 byte)
        packet += b'\x01'                # codigo de funcion (1 byte)
        packet += p16(start_address-1, endian = 'big') #num de coil a leer (2 bytes)
        packet += b'\x00\x01' #número de coils (1 byte) (solo se pide leer uno)
        conn.send(packet)
        response = conn.recv()
        if response[-2] > 0x80: #error al leer
                raise Exception('Codigo de respuesta mayor de 0x80')

        elif response[-1] & 0x01 == 1: #el ultimo bit es 1
                return True
        else:
                return False

def write_coil(conn, uid, start_address, value):
        packet = random.randbytes(2)
        packet += b'\x00\x00'
        packet += b'\x00\x06'
        packet += p8(uid)
        packet += b'\x05'
        packet += p16 (start_address-1, endian = 'big')
        packet += b'\xff\x00' if value else b'\x00\x00' #escribimos ff00 si es true y 0000 si es false según la especificación del protocolo
        conn.send(packet)

def read_hregister (conn, uid, start_address):
        packet = random.randbytes(2)
        packet += b'\x00\x00'
        packet += b'\x00\x06'
        packet += p8(uid)
        packet += b'\x03'
        packet += p16 (start_address-1, endian = 'big')
        packet += b'\x00\x01' #solo se pide leer un registro
        conn.send(packet)
        response = conn.recv()
        return response[-1] #devuelve el ultimo byte, en este caso como leemos valores entre el 1 y el 100 nos sirve
