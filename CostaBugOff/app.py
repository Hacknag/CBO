
import sys
from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from flask_cors import CORS
from oracledb import IntegrityError
from flask import Response
app = Flask(__name__)
CORS(app)
app.secret_key = "cambia-esto-por-algo-secreto-antes-de-entregar"

RUTAS_CLIENTE = (
    "/planes", "/programar-visita", "/informacion", "/inicio-cliente", "/logout",
    "/carrito", "/checkout", "/factura", "/mis-facturas",
)
RUTAS_RRHH = ("/empleados", "/api/empleados", "/logout")
RUTAS_BILLING = (
    "/facturas", "/factura", "/mis-facturas",
    "/reporte_ventas", "/facturas_billing",
    "/logout",
)

#################### Imports Seccion Clientes####################
#################### Imports Seccion Clientes####################
from models.seccion_cliente.clientes import obtener_clientes, buscar_clientes, insertar_cliente, actualizar_cliente, registrar_cliente, eliminar_cliente_logico
from models.seccion_cliente.telefonos_clientes import insertar_telefonos_clientes, actualizar_telefonos_clientes, eliminar_telefono_cliente_logico, obtener_telefonos_clientes
from models.seccion_cliente.correos_clientes import insertar_correos_clientes, actualizar_correos_clientes, eliminar_correo_cliente_logica, obtener_correos_clientes
from models.seccion_cliente.direcciones_clientes import insertar_direcciones_clientes, actualizar_direcciones_clientes, eliminar_direcciones_clientes_logica, obtener_direcciones_clientes

#################### Imports Seccion Recursos Humanos y Seguridad ####################
#################### Imports Seccion Recursos Humanos y Seguridad ####################
from models.seccion_HR_SEC.puestos import insertar_puesto, actualizar_puesto, eliminar_puesto_logico, obtener_puestos_general, buscar_puestos
from models.seccion_HR_SEC.empleados import obtener_empleados, insertar_empleado, actualizar_empleados, obtener_puestos, eliminar_empleados_logica, buscar_empleados
from models.seccion_HR_SEC.telefonos_empleados import  insertar_telefono_empleado, actualizar_telefono_empleado, eliminar_telefono_empleado_logico, obtener_telefonos_empleados
from models.seccion_HR_SEC.correos_empleados import insertar_correo_empleado, actualizar_correo_empleado, eliminar_correo_empleado_logico, obtener_correos_empleados
from models.seccion_HR_SEC.roles_permisos import obtener_roles_permisos, obtener_roles, obtener_permisos, insertar_permiso_x_rol, eliminar_permiso_x_rol_logico
from models.seccion_HR_SEC.usuarios import obtener_usuarios, eliminar_usuario_logico, insertar_usuario

#################### Imports Seccion Inventario y Proveedores ####################
#################### Imports Seccion Inventario y Proveedores ####################
from models.seccion_inventario.productos import insertar_producto, actualizar_producto, eliminar_producto_logico, obtener_productos
from models.seccion_inventario.productos_x_proveedor import insertar_producto_x_proveedor, eliminar_producto_x_proveedor_logico, obtener_productos_x_proveedor
from models.seccion_inventario.proveedores import insertar_proveedor, actualizar_proveedor, eliminar_proveedor_logico, obtener_proveedores
from models.seccion_inventario.telefonos_proveedores import insertar_telefonos_proveedores, actualizar_telefonos_proveedores, eliminar_telefonos_proveedores_logica, obtener_telefonos_proveedores
from models.seccion_inventario.correos_proveedores import insertar_correo_proveedor, actualizar_correo_proveedor, eliminar_correo_proveedor_logico, obtener_correos_proveedores
from models.seccion_inventario.reabastecimiento_inventario import insertar_reabastecimiento, actualizar_reabastecimiento, eliminar_reabastecimiento_logico, obtener_reabastecimientos

#################### Imports Seccion Operaciones ####################
#################### Imports Seccion Operaciones ####################
from models.seccion_operaciones.plagas import obtener_plagas, insertar_plaga, actualizar_plaga, eliminar_plaga_logica
from models.seccion_operaciones.servicios import insertar_servicio, actualizar_servicio, eliminar_servicio_logico, obtener_servicios   
from models.seccion_operaciones.servicios_realizados import insertar_servicio_realizado, actualizar_servicio_realizado, obtener_servicios_realizados, eliminar_servicio_realizado_logico
from models.seccion_operaciones.visitas import obtener_visitas, insertar_visita, actualizar_visita, eliminar_visita_logica
from models.seccion_operaciones.cantones import insertar_canton, actualizar_canton, eliminar_cantones_logico, obtener_cantones, buscar_cantones
from models.seccion_operaciones.provincias import insertar_provincia, actualizar_provincia, eliminar_provincia_logico, obtener_provincia, buscar_provincias
from models.seccion_operaciones.distritos import obtener_distritos, insertar_distrito, actualizar_distrito, eliminar_distrito_logico

#################### Imports Seccion Facturacion y Finanzas ####################
#################### Imports Seccion Facturacion y Finanzas ####################
from models.seccion_fyf.suscripciones import insertar_suscripcion, actualizar_suscripcion, eliminar_suscripcion, obtener_suscripciones
from models.seccion_fyf.metodos_pago import insertar_metodos_pago, actualizar_metodos_pago, eliminar_metodo_pago_logico, obtener_metodos_pago_main
from models.seccion_fyf.pagos import insertar_pago, actualizar_pago, eliminar_pago, obtener_pagos
from models.seccion_fyf.transacciones import insertar_transaccion, actualizar_transaccion, eliminar_transaccion, obtener_transacciones
from models.seccion_fyf.detalle_transacciones import insertar_detalle_transaccion, actualizar_detalle_transaccion, eliminar_detalle_transaccion, obtener_detalle_transacciones
from models.seccion_fyf.facturas import (
    obtener_metodos_pago, procesar_checkout, obtener_factura,
    obtener_detalle_factura, obtener_facturas_cliente, obtener_todas_facturas, eliminar_factura_logico
)
from models.seccion_fyf.reporte_ventas import obtener_reporte_ventas



from models.usuario import autenticar_usuario
from models.estado import obtener_estados
from models.pdf_factura import generar_pdf_factura
from models.olvide_password import generar_password, send_email, actualizar_usuario, get_usuario_id
from models.contacto import enviar_correo_contacto



###########################################################################################
#################################### SECCION - CLIENTES ###################################
###########################################################################################
# ---------------- Clientes (vista para Admin/Empleado) ----------------
# ---------------- Clientes (vista para Admin/Empleado) ----------------
# ---------------- Clientes (vista para Admin/Empleado) ----------------
@app.route("/")
@app.route("/index")
def clientes():
    lista_clientes = obtener_clientes()
    return render_template("index.html", clientes=lista_clientes)

#INSERT
#INSERT


@app.route("/clientes/agregar", methods=["POST"])
def agregar_cliente():
    try:
        insertar_cliente( 
            nombre=request.form["nombre"],
            apellido_paterno=request.form["apellido_paterno"],
            apellido_materno=request.form["apellido_materno"],
            fecha_registro=None,
            id_estado=int(request.form["id_estado"]),
        )
        return jsonify({"success": True, "message": "Cliente agregado exitosamente"}), 200
    except Exception as e:
        return jsonify({"success": False, "message": f"Error al guardar: {str(e)}"}), 400
    

#UPDATE
#UPDATE
@app.route("/api/clientes/actualizar", methods=["POST"])
def api_actualizar_cliente():
    datos = request.get_json()
    try:
        actualizar_cliente(
            id_cliente=datos["id_cliente"],
            nombre=datos["nombre"],
            apellido_paterno=datos["apellido_paterno"],
            apellido_materno=datos["apellido_materno"],
            id_estado=1
        )
        return jsonify({"success": True, "message": "¡Cliente actualizado con éxito!"}), 200
    except Exception as e:
        return jsonify({"success": False, "message": f"Error al actualizar: {str(e)}"}), 500

#DELETE
#DELETE 
@app.route('/delete/cliente/<int:id_cliente>', methods=['POST'])
def eliminar_cliente(id_cliente):
    try:
        eliminar_cliente_logico(id_cliente)
        return jsonify({'success': True, 'message': 'Cliente eliminado correctamente'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

#BUSCAR
#BUSCAR 
@app.route('/clientes/buscar', methods=['GET'])
def api_buscar_clientes():
    # 1. Extraer el parámetro 'q' de la URL
    query = request.args.get('q', '').strip()    
    # 2. Llamar a la función del archivo clientes.py
    lista_clientes = buscar_clientes(query)
    # 3. Devolver la respuesta JSON
    return jsonify(lista_clientes)

# ---------------- Telefonos de clientes (vista para Admin/Empleado) ----------------
# ---------------- Telefonos de clientes (vista para Admin/Empleado) ----------------
# ---------------- Telefonos de clientes (vista para Admin/Empleado) ----------------
@app.route('/telefonos_clientes')
def telefonos_clientes():
    datos_telefonos = obtener_telefonos_clientes()    
    return render_template('seccion_clientes/telefonos_clientes.html', telefonos=datos_telefonos)

#INSERT
#INSERT
@app.route("/telefonos_clientes/guardar", methods=["POST"])
def api_guardar_telefono_cliente():
    datos = request.get_json() or {}
    
    id_cliente = datos.get("id_cliente")
    # .strip() elimina espacios accidentales al inicio o al final
    telefono = str(datos.get("telefono") or "").strip()
    tipo = str(datos.get("tipo") or "").strip()
    id_estado = datos.get("id_estado")

    # VALIDACIONES OBLIGATORIAS
    if id_cliente is None:
        return jsonify({"message": "Por favor selecciona un cliente válido."}), 400

    if not telefono:  # Si el teléfono está vacío
        return jsonify({"message": "El número de teléfono es obligatorio."}), 400

    if id_estado is None:
        return jsonify({"message": "Por favor selecciona un estado para el teléfono."}), 400

    try:
        insertar_telefonos_clientes(
            ID_CLIENTE=int(id_cliente),
            TELEFONO=telefono,
            TIPO=tipo,
            ID_ESTADO=int(id_estado)
        )
        return jsonify({"message": "¡Teléfono agregado con éxito!"}), 200

    except Exception as e:
        return jsonify({"message": f"Error al guardar en Base de Datos: {str(e)}"}), 500


#UPDATE
#UPDATE
@app.route("/api/telefonos_clientes/actualizar", methods=["POST"])
def api_actualizar_telefono_cliente():
    datos = request.get_json()
    try:
        actualizar_telefonos_clientes(
            ID_CLIENTE=datos["id_cliente"],
            TELEFONO=datos["telefono"],
            TIPO=datos["tipo"],
            ID_ESTADO=datos["id_estado"]
        )
        return jsonify({"message": "¡Teléfono actualizado con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500

# #DELETE 
@app.route('/delete/telefonos_clientes/<int:id_cliente>/<string:telefono>', methods=['POST'])
def eliminar_telefono_cliente(id_cliente, telefono):
    try:
        eliminar_telefono_cliente_logico(id_cliente, telefono)
        return jsonify({'success': True, 'message': 'Telefono eliminado correctamente'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
  

# ---------------- Correos de clientes (vista para Admin/Empleado) ----------------
# ---------------- Correos de clientes (vista para Admin/Empleado) ----------------
# ---------------- Correos de clientes (vista para Admin/Empleado) ----------------
@app.route('/correos_clientes')
def correos_clientes():
    datos_correos = obtener_correos_clientes()    
    return render_template('seccion_clientes/correos_clientes.html', correos=datos_correos)


@app.route("/correos_clientes/guardar", methods=["POST"])
def api_guardar_correo_cliente():
    datos = request.get_json() or {}
    
    id_cliente = datos.get("id_cliente")
    # .strip() elimina espacios accidentales al inicio o al final
    correo = str(datos.get("correo") or "").strip()
    tipo = str(datos.get("tipo") or "").strip()
    id_estado = datos.get("id_estado")

    # VALIDACIONES OBLIGATORIAS
    if id_cliente is None:
        return jsonify({"message": "Por favor selecciona un cliente válido."}), 400

    if not correo:  # Si el teléfono está vacío
        return jsonify({"message": "El correo es obligatorio."}), 400

    if id_estado is None:
        return jsonify({"message": "Por favor selecciona un estado para el correo."}), 400

    try:
        insertar_correos_clientes(
            ID_CLIENTE=int(id_cliente),
            CORREO=correo,
            TIPO=tipo,
            ID_ESTADO=int(id_estado)
        )
        return jsonify({"message": "¡CORREO agregado con éxito!"}), 200

    except Exception as e:
        return jsonify({"message": f"Error al guardar en Base de Datos: {str(e)}"}), 500


@app.route("/api/correos_clientes/actualizar", methods=["POST"])
def api_actualizar_correo_cliente():
    datos = request.get_json()
    try:
        actualizar_correos_clientes(
            ID_CLIENTE=datos["id_cliente"],
            CORREO=datos["correo"],
            TIPO=datos["tipo"],
            ID_ESTADO=datos["id_estado"]
        )
        return jsonify({"message": "¡Correo actualizado con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500


#DELETE
#DELETE 
@app.route('/delete/correos_clientes/<int:id_cliente>/<string:correo>', methods=['POST'])
def eliminar_correo_cliente(id_cliente, correo):
    try:
        eliminar_correo_cliente_logica(id_cliente, correo)
        return jsonify({'success': True, 'message': 'Correo eliminado correctamente'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

# ---------------- Direcciones de clientes (vista para Admin/Empleado) ----------------
# ---------------- Direcciones de clientes (vista para Admin/Empleado) ----------------
# ---------------- Direcciones de clientes (vista para Admin/Empleado) ----------------
@app.route('/direcciones_clientes')
def direcciones_clientes():
    datos_direcciones = obtener_direcciones_clientes()    
    return render_template('seccion_clientes/direcciones_clientes.html', direcciones=datos_direcciones)

@app.route("/api/direcciones_clientes/guardar", methods=["POST"])
def api_guardar_direccion_cliente():
    datos = request.get_json()
    try:
        insertar_direcciones_clientes(
            ID_CLIENTE=datos["id_cliente"],
            DIRECCION=datos["direccion"],
            TIPO=datos["tipo"],
            ID_ESTADO=datos["id_estado"]
        )
        return jsonify({"message": "¡Dirección agregada con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al guardar en Base de Datos: {str(e)}"}), 500

@app.route("/api/direcciones_clientes/actualizar", methods=["POST"])
def api_actualizar_direccion_cliente():
    datos = request.get_json()
    try:
        actualizar_direcciones_clientes(
            ID_CLIENTE=datos["id_cliente"],
            DIRECCION=datos["direccion"],
            TIPO=datos["tipo"],
            ID_ESTADO=datos["id_estado"]
        )
        return jsonify({"message": "¡Dirección actualizada con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500

     


###########################################################################################
########################## SECCION - RECURSOS HUMANOS Y SEGURIDAD #########################
###########################################################################################
# ---------------- Puestos (vista para Admin/HHRR) ----------------
# ---------------- Puestos (vista para Admin/HHRR) ----------------
# ---------------- Puestos (vista para Admin/HHRR) ----------------
@app.route("/puestos")
def puestos():
    id_estado = request.args.get("estado")  # "1"=Activo (tiene empleados), "2"=Inactivo, vacío=Todos
    lista_puestos = obtener_puestos_general(id_estado)
    return render_template("seccion_HR-SEC/puestos.html", puestos=lista_puestos, filtro=id_estado)


@app.route("/puestos/agregar", methods=["POST"])
def agregar_puesto():
    try:
        insertar_puesto(            
            nombre=request.form["puesto"],
            descripcion=request.form["descripcion"],
            id_estado=int(request.form["id_estado"]),
        )
        return jsonify({"success": True, "message": "¡Puesto agregado con éxito!"}), 200
    except Exception as e:
        return jsonify({"success": False, "message": f"Error al guardar en Base de Datos: {str(e)}"}), 500


@app.route("/api/puestos/actualizar", methods=["POST"])
def api_actualizar_puesto():
    datos = request.get_json()
    try:
        actualizar_puesto(
            id_puesto=datos["id_puesto"],
            nombre=datos["nombre"],
            descripcion=datos["descripcion"]
        )
        return jsonify({"message": "¡Puesto actualizado con éxito"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500


@app.route("/delete/puestos/<int:id_puesto>", methods=["POST"])
def api_eliminar_puesto(id_puesto):
    try:
        eliminar_puesto_logico(id_puesto)
        return jsonify({"success": True,"message": "¡Puesto eliminado con éxito!"}), 200
    except Exception as e:
        return jsonify({"success": False,"message": f"Error al eliminar en Base de Datos: {str(e)}"}), 500

#BUSCAR
#BUSCAR 
@app.route('/puestos/buscar', methods=['GET'])
def api_buscar_puestos():
    # 1. Extraer el parámetro 'q' de la URL
    query = request.args.get('q', '').strip()    
    # 2. Llamar a la función del archivo clientes.py
    lista_puestos = buscar_puestos(query)
    # 3. Devolver la respuesta JSON
    return jsonify(lista_puestos)

# ---------------- Empleados (vista para Admin/HHRR) ----------------
# ---------------- Empleados (vista para Admin/HHRR) ----------------
# ---------------- Empleados (vista para Admin/HHRR) ----------------
@app.route("/empleados")
def empleados():
    id_estado = request.args.get("estado")  # "1"=Activo, "2"=Inactivo, vacío=Todos
    lista_empleados = obtener_empleados()
    lista_puestos = obtener_puestos()
    return render_template("seccion_HR-SEC/empleados.html", empleados=lista_empleados, filtro=id_estado, puestos=lista_puestos)


@app.route("/empleados/guardar", methods=["POST"])
def agregar_empleado():
    datos = request.get_json()
    try:
        insertar_empleado(
            nombre=datos["nombre"],
            apellido_paterno=datos["apellido_paterno"],
            apellido_materno=datos["apellido_materno"],
            id_puesto=datos["id_puesto"],
            id_estado = 1
        )
        return jsonify({"message": "¡Empleado agregado con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al guardar en Base de Datos: {str(e)}"}), 500


@app.route("/api/empleados/actualizar", methods=["POST"])
def api_actualizar_empleado():
    datos = request.get_json()
    try:
        actualizar_empleados(
            id_empleado=datos["id_empleado"],
            nombre=datos["nombre"],
            apellido_paterno=datos["apellido_paterno"],
            apellido_materno=datos["apellido_materno"],
            id_puesto=datos["id_puesto"],
            id_estado= 1 
        )
        return jsonify({"message": "¡Empleado actualizado con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500


@app.route("/delete/empleados/<int:id_empleado>", methods=["POST"])
def desactivar_empleado(id_empleado):
    try:
        eliminar_empleados_logica(id_empleado)
        return jsonify({'success': True, 'message': '¡Empleado desactivado con éxito!'}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': f"Error al desactivar en Base de Datos: {str(e)}"}), 500


#BUSCAR
#BUSCAR 
@app.route('/empleados/buscar', methods=['GET'])
def api_buscar_empleados():
    # 1. Extraer el parámetro 'q' de la URL
    query = request.args.get('q', '').strip()    
    print(f"--> Búsqueda recibida en Flask: '{query}'") # Impresión de prueba
    # 2. Llamar a la función del archivo clientes.py
    lista_empleados = buscar_empleados(query)
    print(f"--> Empleados encontrados: {lista_empleados}") # Impresión de prueba
    # 3. Devolver la respuesta JSON
    return jsonify(lista_empleados)

# ---------------- Telefonos de Empleados (vista para Admin/Empleado) ----------------
# ---------------- Telefonos de Empleados (vista para Admin/Empleado) ----------------
# ---------------- Telefonos de Empleados (vista para Admin/Empleado) ----------------
@app.route('/telefonos_empleados')
def telefonos_empleados():
    datos_telefonos = obtener_telefonos_empleados()    
    return render_template('seccion_HR-SEC/telefonos_empleados.html', telefonos=datos_telefonos)

#INSERT
#INSERT
@app.route("/telefonos_empleados/guardar", methods=["POST"])
def api_guardar_telefono_empleado():
    datos = request.get_json() or {}
    
    id_empleado = datos.get("id_empleado")
    # .strip() elimina espacios accidentales al inicio o al final
    telefono = str(datos.get("telefono") or "").strip()
    tipo = str(datos.get("tipo") or "").strip()
    id_estado = datos.get("id_estado")

    # VALIDACIONES OBLIGATORIAS
    if id_empleado is None:
        return jsonify({"message": "Por favor selecciona un empleado válido."}), 400

    if not telefono:  # Si el teléfono está vacío
        return jsonify({"message": "El número de teléfono es obligatorio."}), 400

    if id_estado is None:
        return jsonify({"message": "Por favor selecciona un estado para el teléfono."}), 400

    try:
        insertar_telefono_empleado(
            ID_EMPLEADO=int(id_empleado),
            TELEFONO=telefono,
            TIPO=tipo,
            ID_ESTADO=int(id_estado)
        )
        return jsonify({"message": "¡Teléfono agregado con éxito!"}), 200

    except Exception as e:
        return jsonify({"message": f"Error al guardar en Base de Datos: {str(e)}"}), 500


#UPDATE
#UPDATE
@app.route("/api/telefonos_empleados/actualizar", methods=["POST"])
def api_actualizar_telefono_empleado():
    datos = request.get_json()
    try:
        actualizar_telefono_empleado(
            ID_EMPLEADO=datos["id_empleado"],
            TELEFONO=datos["telefono"],
            TIPO=datos["tipo"],
            ID_ESTADO=datos["id_estado"]
        )
        return jsonify({"message": "¡Teléfono actualizado con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500

# #DELETE 
@app.route('/delete/telefonos_empleados/<int:id_empleado>/<string:telefono>', methods=['POST'])
def eliminar_telefono_empleado(id_empleado, telefono):
    try:
        eliminar_telefono_empleado_logico(id_empleado, telefono)
        return jsonify({'success': True, 'message': 'Telefono eliminado correctamente'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
  

# ---------------- Correos Empleados (vista para Admin/HHRR) ----------------
# ---------------- Correos Empleados (vista para Admin/HHRR) ----------------
# ---------------- Correos Empleados (vista para Admin/HHRR) ----------------
@app.route('/correos_empleados')
def correos_empleados():
    datos_correos = obtener_correos_empleados()    
    return render_template('seccion_HR-SEC/correos_empleados.html', correos=datos_correos)

@app.route("/correos_empleados/guardar", methods=["POST"])
def api_guardar_correo_empleado():
    datos = request.get_json()
    try:
        insertar_correo_empleado(
            ID_EMPLEADO=datos["id_empleado"],
            CORREO=datos["correo"],
            TIPO=datos["tipo"],
            ID_ESTADO=datos["id_estado"]
        )
        return jsonify({"message": "¡Correo agregado con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al guardar en Base de Datos: {str(e)}"}), 500

@app.route("/api/correos_empleados/actualizar", methods=["POST"])
def api_actualizar_correo_empleado():
    datos = request.get_json()
    try:
        actualizar_correo_empleado(
            ID_EMPLEADO=datos["id_empleado"],
            CORREO=datos["correo"],
            TIPO=datos["tipo"],
            ID_ESTADO=datos["id_estado"]
        )
        return jsonify({"message": "¡Correo actualizado con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500

#DELETE
#DELETE 
@app.route('/delete/correos_empleados/<int:id_empleado>/<string:correo>', methods=['POST'])
def eliminar_correo_empleado(id_empleado, correo):
    try:
        eliminar_correo_empleado_logico(id_empleado, correo)
        return jsonify({'success': True, 'message': 'Correo eliminado correctamente'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

# ---------------- Roles y Permisos  ----------------
# ---------------- Roles y Permisos   ----------------
# ---------------- Roles y Permisos  ----------------
@app.route("/roles_permisos")
def roles_permisos():
    lista_roles_permisos = obtener_roles_permisos()
    lista_roles = obtener_roles()
    lista_permisos = obtener_permisos()
    return render_template(
        "seccion_HR-SEC/roles_permisos.html",
        roles_permisos=lista_roles_permisos,
        roles=lista_roles,
        permisos=lista_permisos,
    )

@app.route("/api/roles_permisos/guardar", methods=["POST"])
def api_guardar_rol_permiso():
    datos = request.get_json()
    try:
        insertar_permiso_x_rol(
            id_rol=datos["id_rol"],
            id_permiso=datos["id_permiso"]
        )
        return jsonify({"message": "¡Permiso asignado al rol con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al guardar en Base de Datos: {str(e)}"}), 500

@app.route("/api/roles_permisos/eliminar/<int:id_rol>/<int:id_permiso>", methods=["POST"])
def api_eliminar_rol_permiso(id_rol, id_permiso):
    try:
        eliminar_permiso_x_rol_logico(id_rol, id_permiso)
        return jsonify({"message": "¡Permiso removido del rol con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al eliminar en Base de Datos: {str(e)}"}), 500


# ---------------- Usuarios (vista para Admin/HHRR) ----------------
# ---------------- Usuarios (vista para Admin/HHRR) ----------------
# ---------------- Usuarios (vista para Admin/HHRR) ----------------
@app.route("/usuarios")
def usuarios():
    lista_usuarios = obtener_usuarios()
    return render_template("seccion_HR-SEC/usuarios.html", usuarios=lista_usuarios)

@app.route("/delete/usuarios/<int:id_usuario>", methods=["POST"])
def api_eliminar_usuario(id_usuario):
    try:
        eliminar_usuario_logico(id_usuario)
        return jsonify({'success': True, 'message': '¡Usuario desactivado con éxito!'}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': f"Error al desactivar en Base de Datos: {str(e)}"}), 500

# Agregar
@app.route("/usuarios/agregar", methods=["POST"])
def agregar_usuario():
    try:
        # Lee el JSON enviado desde JavaScript
        datos = request.get_json()
        
        if not datos:
            return jsonify({"success": False, "message": "No se recibieron datos válidos."}), 400

        # Pasa los parámetros con los nombres correctos
        insertar_usuario(            
            USUARIO=datos.get("nombre"),
            ID_ROL=int(datos.get("id_rol")),
            ID_ESTADO=int(datos.get("id_estado"))
        )
        return jsonify({"success": True, "message": "¡Usuario creado con éxito!"}), 200

    except ValueError as ve:
        # Captura si el usuario ya existe
        return jsonify({"success": False, "message": str(ve)}), 400
    except Exception as e:
        return jsonify({"success": False, "message": f"Error: {str(e)}"}), 500


###########################################################################################
############################ SECCION - INVENTARIO Y PROVEEDORES ###########################
###########################################################################################
# ---------------- Productos (vista para Admin/Empleado) ----------------
# ---------------- Productos (vista para Admin/Empleado) ----------------
# ---------------- Productos (vista para Admin/Empleado) ----------------
@app.route("/productos")
def productos():
    lista_productos = obtener_productos()
    lista_relaciones = obtener_productos_x_proveedor()
    lista_proveedores = obtener_proveedores()
    return render_template(
        "seccion_inventario/productos.html",
        productos=lista_productos,
        relaciones=lista_relaciones,
        proveedores=lista_proveedores
    )

@app.route("/delete/productos/<int:id_producto>", methods=["POST"])
def eliminar_producto(id_producto):
    try:
        eliminar_producto_logico(id_producto)
        return jsonify({'success': True, 'message': 'Producto eliminado correctamente'}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': f"Error al eliminar en Base de Datos: {str(e)}"}), 500

@app.route("/productos/agregar", methods=["POST"])
def api_guardar_producto():
    try:
        insertar_producto(            
            NOMBRE=request.form["nombre"],
            DESCRIPCION=request.form["descripcion"],
            PRECIO=int(request.form["precio"]),
            UNIDADES_ACTUALES=int(request.form["unidades"]),
            ID_ESTADO=int(request.form["id_estado"]),
        )
        return jsonify({'success': True, "message": "¡Producto agregado con éxito!"}), 200
    except Exception as e:
        return jsonify({'success': False,"message": f"Error al guardar en Base de Datos: {str(e)}"}), 500


@app.route("/api/productos/actualizar", methods=["POST"])
def api_actualizar_producto():
    datos = request.get_json()
    try:
        actualizar_producto(
            id_producto=datos["id_producto"],
            nombre=datos["nombre"],
            descripcion=datos["descripcion"],
            precio=datos["precio"],
            unidades=datos["unidades"],
            id_estado=datos["id_estado"]
        )
        return jsonify({"message": "¡Producto actualizado con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500
    
# ---------------- Productos X Proveedores(vista para Admin/Empleado) ----------------
@app.route("/api/productos-x-proveedor/guardar", methods=["POST"])
def api_guardar_producto_x_proveedor():
    datos = request.get_json()
    try:
        insertar_producto_x_proveedor(
            id_producto=datos["id_producto"],
            id_proveedor=datos["id_proveedor"]
        )
        return jsonify({"message": "¡Relación agregada con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al guardar en Base de Datos: {str(e)}"}), 500


@app.route("/api/productos-x-proveedor/eliminar/<int:id_proveedor>/<int:id_producto>", methods=["POST"])
def api_eliminar_producto_x_proveedor(id_proveedor, id_producto):
    try:
        eliminar_producto_x_proveedor_logico(id_producto, id_proveedor)
        return jsonify({"message": "¡Relación desactivada con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al desactivar en Base de Datos: {str(e)}"}), 500


# ---------------- Reabastecimiento de Inventario ----------------
# ---------------- Reabastecimiento de Inventario ----------------
# ---------------- Reabastecimiento de Inventario ----------------
@app.route("/reabastecimiento_inventario")
def reabastecimiento_inventario():
    id_estado = request.args.get("estado")  # "1"=Activo, "2"=Inactivo, vacío=Todos
    lista_reabastecimientos = obtener_reabastecimientos(id_estado)
    lista_estados = obtener_estados()
    return render_template(
        "seccion_inventario/reabastecimiento_inventario.html",
        reabastecimientos=lista_reabastecimientos,
        estados=lista_estados,
        filtro=id_estado,
    )

@app.route("/api/reabastecimiento_inventario/guardar", methods=["POST"])
def api_guardar_reabastecimiento():
    datos = request.get_json()
    try:
        insertar_reabastecimiento(
            id_reabastecimiento=datos["id_reabastecimiento"],
            cantidad=datos["cantidad"],
            id_estado=datos["id_estado"]
        )
        return jsonify({"message": "¡Reabastecimiento agregado con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al guardar en Base de Datos: {str(e)}"}), 500

@app.route("/api/reabastecimiento_inventario/actualizar", methods=["POST"])
def api_actualizar_reabastecimiento():
    datos = request.get_json()
    try:
        actualizar_reabastecimiento(
            id_reabastecimiento=datos["id_reabastecimiento"],
            cantidad=datos["cantidad"],
            id_estado=datos["id_estado"]
        )
        return jsonify({"message": "¡Reabastecimiento actualizado con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500

@app.route("/api/reabastecimiento_inventario/eliminar/<int:id_reabastecimiento>", methods=["POST"])
def api_eliminar_reabastecimiento(id_reabastecimiento):
    try:
        eliminar_reabastecimiento_logico(id_reabastecimiento)
        return jsonify({"message": "¡Reabastecimiento desactivado con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al desactivar en Base de Datos: {str(e)}"}), 500

# ---------------- Proveedores (vista para Admin/Empleado) ----------------
# ---------------- Proveedores (vista para Admin/Empleado) ----------------
# ---------------- Proveedores (vista para Admin/Empleado) ----------------
@app.route("/proveedores")
def proveedores():
    id_estado = request.args.get("estado")  # "1"=Activo, "2"=Inactivo, vacío=Todos
    lista_proveedores = obtener_proveedores(id_estado)
    return render_template("seccion_inventario/proveedores.html", proveedores=lista_proveedores, filtro=id_estado)

@app.route("/api/proveedores/guardar", methods=["POST"])
def api_guardar_proveedor():
    datos = request.get_json()
    try:
        insertar_proveedor(
            nombre=datos["nombre"],
            id_reabastecimiento=datos.get("id_reabastecimiento"),
            id_estado= 1
        )
        return jsonify({"message": "¡Proveedor agregado con éxito en Oracle!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al guardar en Base de Datos: {str(e)}"}), 500
 
 
@app.route("/api/proveedores/actualizar", methods=["POST"])
def api_actualizar_proveedor():
    datos = request.get_json()
    try:
        actualizar_proveedor(
            id_proveedor=datos["id_proveedor"],
            nombre=datos["nombre"],
            id_reabastecimiento=datos.get("id_reabastecimiento"),
            id_estado=1
        )
        return jsonify({"message": "¡Proveedor actualizado con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500
 
 
@app.route("/delete/proveedores/<int:id_proveedor>", methods=["POST"])
def api_eliminar_proveedor(id_proveedor):
    try:
        eliminar_proveedor_logico(id_proveedor)
        return jsonify({'success': True, 'message': '¡Proveedor desactivado con éxito!'}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': f"Error al desactivar en Base de Datos: {str(e)}"}), 500
 
# ---------------- Telefono Proveedores (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Telefono Proveedores (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Telefono Proveedores (vista para Admin/Empleado/Cliente) ----------------
@app.route("/telefonos_proveedores")
def telefonos_proveedores():
    lista_telefonos = obtener_telefonos_proveedores()
    return render_template("seccion_inventario/telefonos_proveedores.html", telefonos_proveedores=lista_telefonos)

@app.route("/api/telefonos_proveedores/guardar", methods=["POST"])
def api_guardar_telefono_proveedor():
    datos = request.get_json()
    try:
        insertar_telefonos_proveedores(
            id_proveedor=datos["id_proveedor"],
            nombre=datos["nombre"],
            id_estado= 1
        )
        return jsonify({"message": "¡Proveedor agregado con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al guardar en Base de Datos: {str(e)}"}), 500

@app.route("/api/telefonos_proveedores/actualizar", methods=["POST"])
def api_actualizar_telefono_proveedor():
    datos = request.get_json()
    try:
        actualizar_telefonos_proveedores(
            id_proveedor=datos["id_proveedor"],
            nombre=datos["nombre"],
            id_estado=1
        )
        return jsonify({"message": "¡Proveedor actualizado con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500

@app.route("/api/telefonos_proveedores/eliminar/<int:id_proveedor>", methods=["POST"])
def api_eliminar_telefono_proveedor(id_proveedor):
    try:
        eliminar_telefonos_proveedores_logica(id_proveedor)
        return jsonify({"message": "¡Telefono eliminado con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al eliminar en Base de Datos: {str(e)}"}), 500


# ---------------- Correos de proveedores (vista para Admin/Empleado) ----------------
# ---------------- Correos de proveedores (vista para Admin/Empleado) ----------------
# ---------------- Correos de proveedores (vista para Admin/Empleado) ----------------
@app.route('/correos_proveedores')
def correos_proveedores():
    datos_correos = obtener_correos_proveedores()
    lista_proveedores = obtener_proveedores()
    return render_template('seccion_inventario/correos_proveedores.html', correos=datos_correos, proveedores=lista_proveedores)
 
@app.route("/delete/correos_proveedores/<int:id_proveedor>/<string:correo>", methods=["POST"])
def api_eliminar_correo_proveedor(id_proveedor, correo):
    try:
        eliminar_correo_proveedor_logico(id_proveedor, correo)
        return jsonify({"success": True, "message": "Correo eliminado correctamente"}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
 
@app.route("/api/correos_proveedores/guardar", methods=["POST"])
def api_guardar_correo_proveedor():
    datos = request.get_json()
    try:
        insertar_correo_proveedor(
            id_proveedor=datos["id_proveedor"],
            correo=datos["correo"],
            tipo=datos["tipo"],
            id_estado=datos["id_estado"]
        )
        return jsonify({"message": "¡Correo agregado con éxito en Oracle!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al guardar en Base de Datos: {str(e)}"}), 500
 
@app.route("/api/correos_proveedores/actualizar", methods=["POST"])
def api_actualizar_correo_proveedor():
    datos = request.get_json()
    try:
        actualizar_correo_proveedor(
            id_proveedor=datos["id_proveedor"],
            correo_actual=datos["correo_actual"],
            correo_nuevo=datos["correo_nuevo"],
            tipo=datos["tipo"],
            id_estado=datos["id_estado"]
        )
        return jsonify({"message": "¡Correo actualizado con éxito en Oracle!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500
    
###########################################################################################
################################## SECCION - OPERACIONES ##################################
###########################################################################################
# ---------------- Telefono Plagas (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Telefono Plagas (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Telefono Plagas (vista para Admin/Empleado/Cliente) ----------------
@app.route("/plagas")
def plagas():
    lista_plagas = obtener_plagas() 
    return render_template("seccion_operaciones/plagas.html", plagas=lista_plagas)

@app.route('/delete/plagas/<int:id_plaga>', methods=['POST'])
def eliminar_plaga(id_plaga):
    try:
        eliminar_plaga_logica(id_plaga)
        return jsonify({'success': True, 'message': 'Plaga eliminada correctamente'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
    


# ---------------- Servicios (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Servicios (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Servicios (vista para Admin/Empleado/Cliente) ----------------
@app.route("/servicios")
def servicios():
    id_estado = request.args.get("estado")  # vacío = Todos, o el ID de cualquier estado del catálogo
    lista_servicios = obtener_servicios(id_estado)
    return render_template("seccion_operaciones/servicios.html", servicios=lista_servicios, filtro=id_estado)


@app.route('/delete/servicios/<int:id_servicio>', methods=['POST'])
def eliminar_servicio(id_servicio):
    try:
        eliminar_servicio_logico(id_servicio)
        return jsonify({'success': True, 'message': 'Servicio eliminado correctamente'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
    


# ---------------- Servicios Realizados (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Servicios Realizados (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Servicios Realizados (vista para Admin/Empleado/Cliente) ----------------
@app.route("/servicios_realizados")
def servicios_realizados():
    id_estado = request.args.get("estado")  # vacío = Todos, o el ID de cualquier estado del catálogo
    lista_servicios_realizados = obtener_servicios_realizados(id_estado)
    lista_estados = obtener_estados()
    return render_template("seccion_operaciones/servicios_realizados.html", serviciosr=lista_servicios_realizados, filtro=id_estado, estados=lista_estados)


@app.route("/api/servicios_realizados/guardar", methods=["POST"])
def api_guardar_servicio_realizado():
    datos = request.get_json()
    try:
        insertar_servicio_realizado(
            id_servicio_realizado=datos["id_servicio_realizado"],
            ubicacion=datos["ubicacion"],
            informe=datos["informe"],
            id_estado=datos["id_estado"]
        )
        return jsonify({"message": "¡Servicio registrado con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al guardar en Base de Datos: {str(e)}"}), 500


@app.route("/api/servicios_realizados/actualizar", methods=["POST"])
def api_actualizar_servicio_realizado():
    datos = request.get_json()
    try:
        actualizar_servicio_realizado(
            id_servicio_realizado=datos["id_servicio_realizado"],
            ubicacion=datos["ubicacion"],
            informe=datos["informe"],
            id_estado=datos["id_estado"]
        )
        return jsonify({"message": "¡Servicio actualizado con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500

@app.route('/delete/servicios_realizados/<int:id_servicio_realizado>', methods=['POST'])
def eliminar_servicio_realizado(id_servicio_realizado):
    try:
        eliminar_servicio_realizado_logico(id_servicio_realizado)
        return jsonify({'success': True, 'message': 'Servicio eliminado correctamente'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
    

# ---------------- Visitas (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Visitas (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Visitas (vista para Admin/Empleado/Cliente) ----------------
@app.route("/visitas")
def visitas():
    lista_visitas = obtener_visitas()
    return render_template("seccion_operaciones/visitas.html", visitas=lista_visitas)

@app.route('/delete/visitas/<int:id_visita>', methods=['POST'])
def eliminar_visita(id_visita):
    try:
        eliminar_visita_logica(id_visita)
        return jsonify({'success': True, 'message': 'Visita eliminada correctamente'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
    
# ---------------- Provincias (vista para Admin) ----------------
# ---------------- Provincias (vista para Admin) ----------------
# ---------------- Provincias (vista para Admin) ----------------

@app.route("/provincias")
def provincias():
    lista_provincias = obtener_provincia()
    return render_template("seccion_operaciones/provincias.html", provincias=lista_provincias)

@app.route("/delete/provincias/<int:id_provincia>", methods=["POST"])
def eliminar_provincia(id_provincia):
    try:
        eliminar_provincia_logico(id_provincia)
        return jsonify({'success': True, 'message': 'Provincia desactivada con éxito!'}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': f"Error al desactivar en Base de Datos: {str(e)}"}), 500

@app.route("/api/provincias/guardar", methods=["POST"])
def guardar_provincia():
    datos = request.get_json()
    try:
        insertar_provincia(
            nombre=datos["nombre"],
            id_estado=datos["id_estado"]
        )
        return jsonify({'success': True,"message": "¡Provincia agregada con éxito!"}), 200
    except Exception as e:
        return jsonify({'success': False, "message": f"Error al guardar en Base de Datos: {str(e)}"}), 500

@app.route("/api/provincias/actualizar", methods=["POST"])
def api_actualizar_provincia():
    datos = request.get_json()
    try:
        actualizar_provincia(
            id_provincia=datos["id_provincia"],
            nombre=datos["nombre"],
            id_estado=datos["id_estado"]
        )
        return jsonify({'success': True, "message": "¡Provincia actualizada con éxito!"}), 200
    except Exception as e:
        return jsonify({'success': False, "message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500
 
@app.route('/provincias/buscar', methods=['GET'])
def api_buscar_provincias():
    # 1. Extraer el parámetro 'q' de la URL
    query = request.args.get('q', '').strip()    
    # 2. Llamar a la función del archivo clientes.py
    lista_provincia = buscar_provincias(query)
    # 3. Devolver la respuesta JSON
    return jsonify(lista_provincia)


# ---------------- Cantones (vista para Admin) ----------------
# ---------------- Cantones (vista para Admin) ----------------
# ---------------- Cantones (vista para Admin) ----------------
@app.route("/cantones")
def cantones():
    lista_cantones = obtener_cantones()
    return render_template("seccion_operaciones/cantones.html", cantones=lista_cantones)

@app.route("/delete/cantones/<int:id_canton>", methods=["POST"])
def eliminar_canton(id_canton):
    try:
        eliminar_cantones_logico(id_canton)
        return jsonify({'success': True, 'message': 'Canton desactivado con éxito!'}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': f"Error al desactivar en Base de Datos: {str(e)}"}), 500
    
@app.route("/api/cantones/guardar", methods=["POST"])
def guardar_canton():
    datos = request.get_json()
    try:
        insertar_canton(            
            nombre=datos["nombre"],
            id_estado=datos["id_estado"]
        )
        return jsonify({'success': True,"message": "¡Canton agregado con éxito!"}), 200
    except Exception as e:
        return jsonify({'success': False, "message": f"Error al guardar en Base de Datos: {str(e)}"}), 500

@app.route("/api/cantones/actualizar", methods=["POST"])
def api_actualizar_canton():
    datos = request.get_json()
    try:
        actualizar_canton(
            id_canton=datos["id_canton"],
            nombre=datos["nombre"],
            id_estado=datos["id_estado"]
        )
        return jsonify({'success': True, "message": "¡Canton actualizado con éxito!"}), 200
    except Exception as e:
        return jsonify({'success': False, "message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500

@app.route('/cantones/buscar', methods=['GET'])
def api_buscar_cantones():
    # 1. Extraer el parámetro 'q' de la URL
    query = request.args.get('q', '').strip()    
    # 2. Llamar a la función del archivo clientes.py
    lista_canton = buscar_cantones(query)
    # 3. Devolver la respuesta JSON
    return jsonify(lista_canton)




# ---------------- Distritos (vista para Admin) ----------------
# ---------------- Distritos (vista para Admin) ----------------
# ---------------- Distritos (vista para Admin) ----------------
@app.route("/distritos")
def distritos():
    lista_distritos = obtener_distritos()
    return render_template("seccion_operaciones/distritos.html", distritos=lista_distritos)

@app.route("/delete/distritos/<int:id_distrito>", methods=["POST"])
def eliminar_distrito(id_distrito):
    try:
        eliminar_distrito_logico(id_distrito)
        return jsonify({'success': True, 'message': 'Distrito desactivado con éxito!'}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': f"Error al desactivar en Base de Datos: {str(e)}"}), 500

@app.route("/api/distritos/guardar", methods=["POST"])
def guardar_distrito():
    datos = request.get_json()
    try:
        insertar_distrito(            
            nombre=datos["nombre"],
            id_estado=datos["id_estado"]
        )
        return jsonify({'success': True,"message": "¡Distrito agregado con éxito!"}), 200
    except Exception as e:
        return jsonify({'success': False, "message": f"Error al guardar en Base de Datos: {str(e)}"}), 500

@app.route("/api/distritos/actualizar", methods=["POST"])
def api_actualizar_distrito():
    datos = request.get_json()
    try:
        actualizar_distrito(
            id_distrito=datos["id_distrito"],
            nombre=datos["nombre"],
            id_estado=datos["id_estado"]
        )
        return jsonify({'success': True, "message": "¡Distrito actualizado con éxito!"}), 200
    except Exception as e:
        return jsonify({'success': False, "message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500
 
 
###########################################################################################
############################# SECCION - FACTURACION Y FINANZAS ############################
###########################################################################################
# ---------------- Suscripciones (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Suscripciones (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Suscripciones (vista para Admin/Empleado/Cliente) ----------------
@app.route("/suscripciones")
def suscripciones():
    lista_suscripciones = obtener_suscripciones()
    return render_template("seccion_fyf/suscripciones.html", suscripciones=lista_suscripciones)
@app.route("/api/suscripciones/guardar", methods=["POST"])

def api_guardar_suscripcion():
    datos = request.get_json()
    insertar_suscripcion(
        id_suscripcion=datos["id_suscripcion"],
        nombre=datos["nombre"],                        # <-- no existe ese parametro
        id_reabastecimiento=datos.get("id_reabastecimiento"),  # <-- tampoco
        id_estado= 1                                    # <-- se llama "Estado", no "id_estado"
    )
 

@app.route("/api/suscripciones/actualizar", methods=["POST"])
def api_actualizar_suscripcion():
    datos = request.get_json()
    try:
        actualizar_suscripcion(
            id_suscripcion=datos["id_suscripcion"],
            nombre=datos["nombre"],
            id_reabastecimiento=datos.get("id_reabastecimiento"),
            id_estado=1
        )
        return jsonify({"message": "¡Suscripción actualizada con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500


@app.route("/api/suscripciones/eliminar/<int:id_suscripcion>", methods=["POST"])
def api_eliminar_suscripcion(id_suscripcion):
    try:
        eliminar_suscripcion(id_suscripcion)
        return jsonify({"message": "¡Suscripción eliminada con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al eliminar en Base de Datos: {str(e)}"}), 500

# ---------------- Metodos de Pago (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Metodos de Pago (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Metodos de Pago (vista para Admin/Empleado/Cliente) ----------------
@app.route("/metodos_pago")
def metodos_pago():
    lista_metodos = obtener_metodos_pago_main()
    return render_template("seccion_fyf/metodos_pago.html", metodos_pago=lista_metodos)

@app.route("/delete/metodos_pago/<int:id_metodo_pago>", methods=["POST"])
def eliminar_metodo_pago(id_metodo_pago):
    try:
        eliminar_metodo_pago_logico(id_metodo_pago)
        return jsonify({'success': True, 'message': 'Método de pago desactivado con éxito!'}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': f"Error al desactivar en Base de Datos: {str(e)}"}), 500
 
@app.route("/api/metodos_pago/guardar", methods=["POST"])
def api_guardar_metodo_pago():
    datos = request.get_json()
    try:
        insertar_metodos_pago(
            NOMBRE=datos["nombre"],
            ID_ESTADO=datos["id_estado"]
        )
        return jsonify({'success': True, "message": "¡Método de pago agregado con éxito!"}), 200
    except Exception as e:
        return jsonify({'success': False, "message": f"Error al guardar en Base de Datos: {str(e)}"}), 500
 
@app.route("/api/metodos_pago/actualizar", methods=["POST"])
def api_actualizar_metodo_pago():
    datos = request.get_json()
    try:
        actualizar_metodos_pago(
            ID_METODO_PAGO=datos["id_metodo_pago"],
            NOMBRE=datos["nombre"],
            ID_ESTADO=datos["id_estado"]
        )
        return jsonify({'success': True, "message": "¡Método de pago actualizado con éxito!"}), 200
    except Exception as e:
        return jsonify({'success': False, "message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500

# ---------------- Pagos (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Pagos (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Pagos (vista para Admin/Empleado/Cliente) ----------------
@app.route("/pagos")
def pagos():
    lista_pagos = obtener_pagos()
    lista_metodos_pago = obtener_metodos_pago_main()
    return render_template("seccion_fyf/pagos.html", pagos=lista_pagos)

@app.route("/api/pagos/guardar", methods=["POST"])
def api_guardar_pago():
    datos = request.get_json()
    try:
        insertar_pago(
            id_pago=datos["id_pago"],
            fecha=datos["fecha"],
            id_metodo_pago=datos["id_metodo_pago"],
            id_estado=datos.get("id_estado", 1)
        )
        return jsonify({"message": "¡Pago agregado con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al guardar en Base de Datos: {str(e)}"}), 500


@app.route("/api/pagos/actualizar", methods=["POST"])
def api_actualizar_pago():
    datos = request.get_json()
    try:
        actualizar_pago(
            id_pago=datos["id_pago"],
            nombre=datos["nombre"],
            id_reabastecimiento=datos.get("id_reabastecimiento"),
            id_estado=1
        )
        return jsonify({"message": "¡Pago actualizado con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500


@app.route("/api/pagos/eliminar/<int:id_pago>", methods=["POST"])
def api_eliminar_pago(id_pago):
    try:
        eliminar_pago(id_pago)
        return jsonify({"message": "¡Pago eliminado con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al eliminar en Base de Datos: {str(e)}"}), 500
# @app.route("/pagos")
# def pagos():
#     lista_pagos = obtener_pagos()
#     return render_template("seccion_fyf/pagos.html", pagos=lista_pagos)

# @app.route("/api/pagos/guardar", methods=["POST"])
# def api_guardar_pago():
#     datos = request.get_json()
#     try:
#         insertar_pago(
#             id_pago=datos["id_pago"],
#             nombre=datos["nombre"],
#             id_reabastecimiento=datos.get("id_reabastecimiento"),
#             id_estado= 1
#         )
#         return jsonify({"message": "¡Pago agregado con éxito!"}), 200
#     except Exception as e:
#         return jsonify({"message": f"Error al guardar en Base de Datos: {str(e)}"}), 500


# @app.route("/api/pagos/actualizar", methods=["POST"])
# def api_actualizar_pago():
#     datos = request.get_json()
#     try:
#         actualizar_pago(
#             id_pago=datos["id_pago"],
#             nombre=datos["nombre"],
#             id_reabastecimiento=datos.get("id_reabastecimiento"),
#             id_estado=1
#         )
#         return jsonify({"message": "¡Pago actualizado con éxito!"}), 200
#     except Exception as e:
#         return jsonify({"message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500


# @app.route("/api/pagos/eliminar/<int:id_pago>", methods=["POST"])
# def api_eliminar_pago(id_pago):
#     try:
#         eliminar_pago(id_pago)
#         return jsonify({"message": "¡Pago eliminado con éxito!"}), 200
#     except Exception as e:
#         return jsonify({"message": f"Error al eliminar en Base de Datos: {str(e)}"}), 500



# ---------------- Transacciones (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Transacciones (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Transacciones (vista para Admin/Empleado/Cliente) ----------------
@app.route("/transacciones")
def transacciones():
    lista_transacciones = obtener_transacciones() 
    return render_template("seccion_fyf/transacciones.html", transacciones=lista_transacciones)

@app.route("/api/transacciones/guardar", methods=["POST"])
def api_guardar_transaccion():
    datos = request.get_json()
    try:
        insertar_transaccion(
            id_transaccion=datos["id_transaccion"],
            nombre=datos["nombre"],
            id_reabastecimiento=datos.get("id_reabastecimiento"),
            id_estado= 1
        )
        return jsonify({"message": "¡Transacción agregada con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al guardar en Base de Datos: {str(e)}"}), 500


@app.route("/api/transacciones/actualizar", methods=["POST"])
def api_actualizar_transaccion():
    datos = request.get_json()
    try:
        actualizar_transaccion(
            id_transaccion=datos["id_transaccion"],
            nombre=datos["nombre"],
            id_reabastecimiento=datos.get("id_reabastecimiento"),
            id_estado=1
        )
        return jsonify({"message": "¡Transacción actualizada con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500


@app.route("/api/transacciones/eliminar/<int:id_transaccion>", methods=["POST"])
def api_eliminar_transaccion(id_transaccion):
    try:
        eliminar_transaccion(id_transaccion)
        return jsonify({"message": "¡Transacción eliminada con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al eliminar en Base de Datos: {str(e)}"}), 500

# ---------------- Detalle de Transacciones (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Detalle de Transacciones (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Detalle de Transacciones (vista para Admin/Empleado/Cliente) ----------------
@app.route("/detalle_transacciones")
def detalle_transacciones():
    lista_detalle = obtener_detalle_transacciones()
    return render_template("seccion_fyf/detalle_transacciones.html", detalle_transacciones=lista_detalle)

@app.route("/api/proveedores/guardar", methods=["POST"])
def api_guardar_proveedor_detalle():
    datos = request.get_json()
    try:
        insertar_proveedor(
            id_proveedor=datos["id_proveedor"],
            nombre=datos["nombre"],
            id_reabastecimiento=datos.get("id_reabastecimiento"),
            id_estado= 1
        )
        return jsonify({"message": "¡Proveedor agregado con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al guardar en Base de Datos: {str(e)}"}), 500


@app.route("/api/detalle_transacciones/actualizar", methods=["POST"])
def api_actualizar_detalle_transaccion():
    datos = request.get_json()
    try:
        actualizar_detalle_transaccion(
            id_detalle_transaccion=datos["id_detalle_transaccion"],
            detalle=datos["detalle"],
            id_estado=datos["id_estado"],
            id_transaccion=datos["id_transaccion"],
            id_producto=datos["id_producto"],
            id_suscripcion=datos["id_suscripcion"],
            cantidad=datos["cantidad"],
            precio_unitario=datos["precio_unitario"],
            subtotal=datos["subtotal"]
        )
        return jsonify({"message": "¡Detalle de transacción actualizado con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500

@app.route("/delete/detalle_transacciones/<int:id_detalle_transaccion>", methods=["POST"])
def api_eliminar_detalle_transaccion(id_detalle_transaccion):
    try:
        eliminar_detalle_transaccion(id_detalle_transaccion)
        return jsonify({"message": "¡Detalle de transacción eliminado con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al eliminar en Base de Datos: {str(e)}"}), 500


# ---------------- Facturas (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Facturas (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Facturas (vista para Admin/Empleado/Cliente) ----------------
@app.route("/facturas")
def facturas_admin():
    id_cliente = request.args.get("id_cliente", type=int)
    clientes = sorted(
        obtener_clientes(),
        key=lambda c: ((c[1] or ""), (c[2] or ""), (c[3] or "")),
    )
    if id_cliente:
        facturas = obtener_facturas_cliente(id_cliente)
    else:
        facturas = obtener_todas_facturas()
    return render_template(
        "seccion_fyf/facturas_admin.html",
        facturas=facturas,
        clientes=clientes,
        id_cliente_seleccionado=id_cliente,
    )

@app.route("/facturas_billing")
def facturas_billing():
    id_cliente = request.args.get("id_cliente", type=int)
    clientes = sorted(
        obtener_clientes(),
        key=lambda c: ((c[1] or ""), (c[2] or ""), (c[3] or "")),
    )
    if id_cliente:
        facturas = obtener_facturas_cliente(id_cliente)
    else:
        facturas = obtener_todas_facturas()
    return render_template(
        "seccion_fyf/facturas_billing.html",
        facturas=facturas,
        clientes=clientes,
        id_cliente_seleccionado=id_cliente,
    )


# @app.route("/facturas")
# def facturas_admin():
#     id_cliente = request.args.get("id_cliente", type=int)
#     clientes = sorted(
#         obtener_clientes(),
#         key=lambda c: ((c[1] or ""), (c[2] or ""), (c[3] or "")),
#     )
#     if id_cliente:
#         facturas = obtener_facturas_cliente(id_cliente)
#     else:
#         facturas = obtener_todas_facturas()
#     plantilla = "seccion_fyf/facturas_billing.html" if session.get("rol") == "Billing" else "seccion_fyf/facturas_admin.html"
#     return render_template(
#         plantilla,
#         facturas=facturas,
#         clientes=clientes,
#         id_cliente_seleccionado=id_cliente,
#     )

@app.route("/delete/facturas/<int:id_factura>", methods=["POST"])
def api_eliminar_factura(id_factura):
    try:
        eliminar_factura_logico(id_factura)
        return jsonify({"message": "¡Factura eliminada con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al eliminar en Base de Datos: {str(e)}"}), 500

###########################################################################################
################################# SECCION - FACTURA ADMIN ################################
###########################################################################################
# @app.route("/planes")
# def planes():
#     lista_productos = obtener_productos()
#     lista_suscripciones = obtener_suscripciones()
#     return render_template(
#         "seccion_facturaA/planes.html",
#         productos=lista_productos,
#         suscripciones=lista_suscripciones,
#     )

MESES_NOMBRE = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
    7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre",
}


@app.route("/reporte_ventas")
def reporte_ventas():
    filas = obtener_reporte_ventas()
    ventas = [
        {
            "anio": int(f[0]),
            "mes": int(f[1]),
            "mes_nombre": MESES_NOMBRE.get(int(f[1]), f[1]),
            "total_ventas": f[2],
            "cantidad_transacciones": f[3],
            "ventas_acumuladas": f[4],
        }
        for f in filas
    ]
    return render_template("seccion_fyf/reporte_ventas.html", ventas=ventas)


# # ---------------- Carrito de compras ----------------
# @app.route("/carrito/agregar", methods=["POST"])
# def carrito_agregar():
#     datos = request.get_json()
#     tipo = datos["tipo"]  # "producto" o "suscripcion"
#     item_id = int(datos["id"])
#     nombre = datos["nombre"]
#     precio = float(datos["precio"])
#     cantidad = int(datos.get("cantidad", 1))

#     carrito = session.get("carrito", [])

#     for item in carrito:
#         if item["tipo"] == tipo and item["id"] == item_id:
#             item["cantidad"] += cantidad
#             break
#     else:
#         carrito.append({
#             "tipo": tipo, "id": item_id, "nombre": nombre,
#             "precio_unitario": precio, "cantidad": cantidad,
#         })

#     session["carrito"] = carrito
#     return jsonify({"message": "Agregado al carrito", "total_items": len(carrito)}), 200


# @app.route("/carrito/quitar", methods=["POST"])
# def carrito_quitar():
#     datos = request.get_json()
#     tipo = datos["tipo"]
#     item_id = int(datos["id"])

#     carrito = session.get("carrito", [])
#     carrito = [i for i in carrito if not (i["tipo"] == tipo and i["id"] == item_id)]
#     session["carrito"] = carrito
#     return jsonify({"message": "Quitado del carrito"}), 200

# @app.route("/carrito")
# def carrito():
#     carrito_actual = session.get("carrito", [])
#     total = sum(i["cantidad"] * i["precio_unitario"] for i in carrito_actual)
#     metodos_pago = obtener_metodos_pago()
#     return render_template(
#         "seccion_facturaA/carrito.html",
#         carrito=carrito_actual,
#         total=total,
#         metodos_pago=metodos_pago,
#     )

# @app.route("/mis-facturas")
# def mis_facturas():
#     facturas = obtener_facturas_cliente(session["id_cliente"])
#     return render_template("seccion_facturaA/mis_facturas.html", facturas=facturas)


@app.route("/planes")
def planes():
    lista_productos = obtener_productos()
    lista_suscripciones = obtener_suscripciones()
    return render_template(
        "planes.html",
        productos=lista_productos,
        suscripciones=lista_suscripciones,
    )


# ---------------- Carrito de compras ----------------
@app.route("/carrito/agregar", methods=["POST"])
def carrito_agregar():
    datos = request.get_json()
    tipo = datos["tipo"]  # "producto" o "suscripcion"
    item_id = int(datos["id"])
    nombre = datos["nombre"]
    precio = float(datos["precio"])
    cantidad = int(datos.get("cantidad", 1))

    carrito = session.get("carrito", [])

    for item in carrito:
        if item["tipo"] == tipo and item["id"] == item_id:
            item["cantidad"] += cantidad
            break
    else:
        carrito.append({
            "tipo": tipo, "id": item_id, "nombre": nombre,
            "precio_unitario": precio, "cantidad": cantidad,
        })

    session["carrito"] = carrito
    return jsonify({"message": "Agregado al carrito", "total_items": len(carrito)}), 200


@app.route("/carrito/quitar", methods=["POST"])
def carrito_quitar():
    datos = request.get_json()
    tipo = datos["tipo"]
    item_id = int(datos["id"])

    carrito = session.get("carrito", [])
    carrito = [i for i in carrito if not (i["tipo"] == tipo and i["id"] == item_id)]
    session["carrito"] = carrito
    return jsonify({"message": "Quitado del carrito"}), 200

@app.route("/carrito")
def carrito():
    carrito_actual = session.get("carrito", [])
    total = sum(i["cantidad"] * i["precio_unitario"] for i in carrito_actual)
    metodos_pago = obtener_metodos_pago()
    return render_template(
        "carrito.html",
        carrito=carrito_actual,
        total=total,
        metodos_pago=metodos_pago,
    )

@app.route("/mis-facturas")
def mis_facturas():
    facturas = obtener_facturas_cliente(session["id_cliente"])
    return render_template("mis_facturas.html", facturas=facturas)

###########################################################################################
################################## SECCION - OTROS ##################################
###########################################################################################
# ---------------- OLVIDE PASSWORD (vista para Admin/Empleado/Cliente) ----------------
# ---------------- OLVIDE PASSWORD (vista para Admin/Empleado/Cliente) ----------------
# ---------------- OLVIDE PASSWORD (vista para Admin/Empleado/Cliente) ----------------
@app.route("/olvide-password")
def olvide_password():
    print(f"--> RECEIVED OLVIDE-PASSWORD", flush=True)
    return render_template("olvide_password.html")

# Ruta que recibe la petición Fetch del JavaScript
@app.route('/olvide-password/reset/<email>', methods=['POST'])
def reset_password(email):
    print(f"--> RECEIVED RESET REQUEST FOR: {email}", flush=True)
    try:
        # data = request.get_json()
        # user_email = data.get('email')

        if not email:
            return jsonify({'success': False, 'error': 'El correo es requerido.'}), 400
        
        else:              
            # Llama a la función que está dentro de olvide_password.py
            get_usuario_id(email)

            return jsonify({
                'success': True, 
                'message': 'Nueva contraseña enviada con éxito.'
            }), 200

    except Exception as e:
        app.logger.error(f"--> REQUEST not RECEIVED FOR: {email}")
        return jsonify({'success': False, 'error': str(e)}), 400



# ---------------- LOGIN / INICIO DE SECCION ----------------
# ---------------- LOGIN / INICIO DE SECCION ----------------
# ---------------- LOGIN / INICIO DE SECCION ----------------


@app.before_request
def verificar_acceso():
    if request.path.startswith("/static") or request.path in ("/login", "/registro") or request.path.startswith("/olvide-password"):
        return
    if "id_usuario" not in session:
        return redirect(url_for("login"))

    rol = session.get("rol")

    if rol == "Administrador":
        return None
    
    if rol == "Cliente" and not request.path.startswith(RUTAS_CLIENTE):
        return redirect(url_for("inicio_cliente"))

    if rol == "RRHH" and not request.path.startswith(RUTAS_RRHH):
        return redirect(url_for("empleados"))

    if rol == "Billing" and not request.path.startswith(RUTAS_BILLING):
        return redirect(url_for("facturas_billing"))

    if rol == "Empleado" and request.path.startswith(("/empleados", "/api/empleados", "/reporte-ventas")):
        return redirect(url_for("clientes"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        correo = request.form.get("correo")
        password = request.form.get("password")
        usuario, mensaje = autenticar_usuario(correo, password)
        if usuario:
            session["id_usuario"] = usuario["id_usuario"]
            session["id_cliente"] = usuario["id_cliente"]
            session["correo"] = correo
            session["rol"] = usuario["rol"]
            session["nombre"] = correo
            if usuario["rol"] == "Cliente":
                return redirect(url_for("inicio_cliente"))
            if usuario["rol"] == "RRHH":
                return redirect(url_for("empleados"))
            return redirect(url_for("clientes"))
        return render_template("login.html", error=mensaje)
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# ---------------- Contacto  ----------------
# ---------------- Contacto  ----------------
# ---------------- Contacto ) ----------------
@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        try:
            enviar_correo_contacto(
                nombre=request.form["nombre"],
                correo=request.form["correo"],
                mensaje=request.form["mensaje"],
            )
            return render_template("contacto.html", enviado=True)
        except Exception as e:
            return render_template("contacto.html", error=f"No se pudo enviar el mensaje: {str(e)}")
    return render_template("contacto.html")


# ---------------- Mi Perfil  ----------------
# ---------------- Mi Perfil  ----------------
# ---------------- Mi Perfil  ----------------
@app.route("/mi_perfil", methods=["GET", "POST"])
def mi_perfil():
    rol = session.get("rol")
    cliente = None
    if rol == "Cliente":
        id_cliente = session.get("id_cliente")
        if request.method == "POST":
            try:
                actualizar_cliente(
                    id_cliente=id_cliente,
                    nombre=request.form["nombre"],
                    apellido_paterno=request.form["apellido_paterno"],
                    apellido_materno=request.form["apellido_materno"],
                    id_estado=1,
                )
            except Exception as e:
                cliente = next((c for c in obtener_clientes() if c[0] == id_cliente), None)
                return render_template("mi_perfil.html", cliente=cliente, error=f"No se pudo actualizar el perfil: {str(e)}")
        cliente = next((c for c in obtener_clientes() if c[0] == id_cliente), None)
    return render_template("mi_perfil.html", cliente=cliente)





@app.route("/checkout", methods=["POST"])
def checkout():
    carrito_actual = session.get("carrito", [])
    if not carrito_actual:
        return render_template("carrito.html", carrito=[], total=0,
                                metodos_pago=obtener_metodos_pago(),
                                error="Tu carrito esta vacio.")
    try:
        id_factura, numero = procesar_checkout(
            id_cliente=session["id_cliente"],
            id_metodo_pago=int(request.form["id_metodo_pago"]),
            direccion=request.form["direccion"],
            telefono=request.form["telefono"],
            carrito=carrito_actual,
        )
        session["carrito"] = []
        return redirect(url_for("ver_factura", id_factura=id_factura))
    except Exception as e:
        total = sum(i["cantidad"] * i["precio_unitario"] for i in carrito_actual)
        return render_template(
            "carrito.html", carrito=carrito_actual, total=total,
            metodos_pago=obtener_metodos_pago(),
            error=f"No se pudo procesar el pago: {e}",
        )

@app.route("/factura/<int:id_factura>")
def ver_factura(id_factura):
    factura = obtener_factura(id_factura)
    detalle = obtener_detalle_factura(id_factura)
    plantilla = "factura_cliente.html" if session.get("rol") == "Cliente" else "factura.html"
    return render_template(plantilla, factura=factura, detalle=detalle)

@app.route("/factura/<int:id_factura>/pdf")
def descargar_factura_pdf(id_factura):
    factura = obtener_factura(id_factura)
    detalle = obtener_detalle_factura(id_factura)
    pdf_bytes = generar_pdf_factura(factura, detalle)
    return Response(
        pdf_bytes,
        mimetype="application/pdf",
        headers={"Content-Disposition": f"inline; filename=factura_{factura['NUMERO']}.pdf"},
    )

@app.route("/programar-visita")
def programar_visita():
    return render_template("programar_visita.html")

@app.route("/informacion")
def informacion():
    return render_template("informacion.html")

@app.route("/inicio-cliente")
def inicio_cliente():
    return render_template("home_cliente.html")

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        id_usuario, id_cliente, mensaje = registrar_cliente(
            nombre=request.form["nombre"],
            apellido_paterno=request.form["apellido_paterno"],
            apellido_materno=request.form["apellido_materno"],
            correo=request.form["correo"],
            password=request.form["password"],
        )
        if mensaje == "OK":
            session["id_usuario"] = id_usuario
            session["id_cliente"] = id_cliente
            session["correo"] = request.form["correo"]
            session["rol"] = "Cliente"
            session["nombre"] = request.form["correo"]
            return redirect(url_for("inicio_cliente"))
        return render_template("registro.html", error=mensaje)
    return render_template("registro.html")


####################################################################################################
####################################################################################################
####################################################################################################
#con esto se enciende el server
if __name__ == "__main__":
# se cambio al puerto 5001 porque el 3000 no anda
    app.run(debug=True, port=5001)