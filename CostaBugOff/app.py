from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from flask_cors import CORS
from oracledb import IntegrityError
from flask import Response
from datetime import datetime
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
    "/reporte-ventas",
    "/logout",
)

#################### Imports Seccion Clientes####################
#################### Imports Seccion Clientes####################
from models.seccion_cliente.clientes import obtener_clientes, insertar_cliente, actualizar_cliente, registrar_cliente, eliminar_cliente_logico
from models.seccion_cliente.telefonos_clientes import insertar_telefonos_clientes, actualizar_telefonos_clientes, eliminar_telefonos_clientes_logica, obtener_telefonos_clientes
from models.seccion_cliente.correos_clientes import insertar_correos_clientes, actualizar_correos_clientes, eliminar_correos_clientes_logica, obtener_correos_clientes
from models.seccion_cliente.direcciones_clientes import insertar_direcciones_clientes, actualizar_direcciones_clientes, eliminar_direcciones_clientes_logica, obtener_direcciones_clientes

#################### Imports Seccion Recursos Humanos y Seguridad ####################
#################### Imports Seccion Recursos Humanos y Seguridad ####################
from models.seccion_HR_SEC.puestos import insertar_puesto, actualizar_puesto, eliminar_puesto_logico, obtener_puestos_general
from models.seccion_HR_SEC.empleados import obtener_empleados, insertar_empleados, actualizar_empleados, obtener_puestos, eliminar_empleados_logica
from models.seccion_HR_SEC.correos_empleados import insertar_correo_empleado, actualizar_correo_empleado, eliminar_correo_empleado_logico, obtener_correos_empleados

#################### Imports Seccion Inventario y Proveedores ####################
#################### Imports Seccion Inventario y Proveedores ####################
from models.seccion_inventario.productos import insertar_producto, actualizar_producto, eliminar_producto_logico, obtener_productos
from models.seccion_inventario.productos_x_proveedor import insertar_producto_x_proveedor, eliminar_producto_x_proveedor_logico, obtener_productos_x_proveedor
from models.seccion_inventario.proveedores import insertar_proveedor, actualizar_proveedor, eliminar_proveedor_logico, obtener_proveedores
from models.seccion_inventario.telefonos_proveedores import insertar_telefonos_proveedores, actualizar_telefonos_proveedores, eliminar_telefonos_proveedores_logica, obtener_telefonos_proveedores
from models.seccion_inventario.correos_proveedores import insertar_correo_proveedor, actualizar_correo_proveedor, eliminar_correo_proveedor_logico, obtener_correos_proveedores
#################### Imports Seccion Operaciones ####################
#################### Imports Seccion Operaciones ####################
from models.seccion_operaciones.plagas import obtener_plagas
from models.seccion_operaciones.servicios import insertar_servicio, actualizar_servicio, eliminar_servicio_logico, obtener_servicios
from models.seccion_operaciones.servicios_realizados import insertar_servicio_realizado, actualizar_servicio_realizado, obtener_servicios_realizados
from models.seccion_operaciones.visitas import obtener_visitas
from models.seccion_operaciones.cantones import insertar_canton, actualizar_canton, eliminar_cantones_logico, obtener_cantones
from models.seccion_operaciones.provincias import insertar_provincia, actualizar_provincia, eliminar_provincia_logico, obtener_provincia
from models.seccion_operaciones.distritos import obtener_distritos, insertar_distrito, actualizar_distrito, eliminar_distrito_logico

#################### Imports Seccion Facturacion y Finanzas ####################
#################### Imports Seccion Facturacion y Finanzas ####################
from models.seccion_fyf.suscripciones import insertar_suscripcion, actualizar_suscripcion, eliminar_suscripcion, obtener_suscripciones
from models.seccion_fyf.metodos_pago import insertar_metodos_pago, actualizar_metodos_pago, eliminar_metodos_pago_logica, obtener_metodos_pago_main
from models.seccion_fyf.pagos import insertar_pago, actualizar_pago, eliminar_pago, obtener_pagos
from models.seccion_fyf.transacciones import insertar_transaccion, actualizar_transaccion, eliminar_transaccion, obtener_transacciones
from models.seccion_fyf.detalle_transacciones import insertar_detalle_transaccion, actualizar_detalle_transaccion, eliminar_detalle_transaccion, obtener_detalle_transacciones
from models.seccion_fyf.facturas import (
    obtener_metodos_pago, procesar_checkout, obtener_factura,
    obtener_detalle_factura, obtener_facturas_cliente, obtener_todas_facturas
)
from models.seccion_fyf.reporte_ventas import obtener_reporte_ventas
from models.seccion_fyf.suscripciones_activas import obtener_suscripciones_activas


from models.usuario import autenticar_usuario
from models.estado import obtener_estados
from models.pdf_factura import generar_pdf_factura
from models.olvide_password import generar_password, send_email, actualizar_usuario, get_usuario_id




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
@app.route("/clientes/agregar", methods=["GET", "POST"])
def agregar_cliente():
    if request.method == "POST":
        try:
            insertar_cliente(
                id_cliente=request.form["id_cliente"],
                nombre=request.form["nombre"],
                apellido_paterno=request.form["apellido_paterno"],
                apellido_materno=request.form["apellido_materno"],
                fecha_registro=None,
                id_estado=request.form["id_estado"],
            )
            return redirect(url_for("clientes"))
        except Exception as e:
            return render_template("seccion_clientes/agregar_Clientes.html", error=f"Error al guardar: {e}")
    return render_template("seccion_clientes/agregar_Clientes.html")

#UPDATE
#UPDATE
@app.route("/clientes/editar/<int:id_cliente>", methods=["GET", "POST"])
def editar_cliente(id_cliente):
    if request.method == "POST":
        try:
            actualizar_cliente(
                id_cliente=id_cliente,
                nombre=request.form["nombre"],
                apellido_paterno=request.form["apellido_paterno"],
                apellido_materno=request.form["apellido_materno"],
                id_estado=request.form["id_estado"],
            )
            return redirect(url_for("clientes"))
        except Exception as e:
            cliente = next((c for c in obtener_clientes() if c[0] == id_cliente), None)
            return render_template("editar_Clientes.html", cliente=cliente, error=f"Error al actualizar: {e}")

    cliente = next((c for c in obtener_clientes() if c[0] == id_cliente), None)
    return render_template("seccion_clientes/editar_Clientes.html", cliente=cliente)


#DELETE
#DELETE 
@app.route('/delete/cliente/<int:id_cliente>', methods=['POST'])
def eliminar_cliente(id_cliente):
    try:
        eliminar_cliente_logico(id_cliente)
        return jsonify({'success': True, 'message': 'Cliente eliminado correctamente'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
    
# ---------------- Telefonos de clientes (vista para Admin/Empleado) ----------------
# ---------------- Telefonos de clientes (vista para Admin/Empleado) ----------------
# ---------------- Telefonos de clientes (vista para Admin/Empleado) ----------------
@app.route('/telefonos_clientes')
def telefonos_clientes():
    datos_telefonos = obtener_telefonos_clientes()    
    return render_template('seccion_clientes/telefonos_clientes.html', telefonos=datos_telefonos)

#INSERT
#INSERT
@app.route("/api/telefonos_clientes/guardar", methods=["POST"])
def api_guardar_telefono_cliente():
    datos = request.get_json()
    try:
        insertar_telefonos_clientes(
            ID_CLIENTE=datos["id_cliente"],
            TELEFONO=datos["telefono"],
            TIPO=datos["tipo"],
            ID_ESTADO=datos["id_estado"]
        )
        return jsonify({"message": "¡Teléfono agregado con éxito en Oracle!"}), 200
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
        return jsonify({"message": "¡Teléfono actualizado con éxito en Oracle!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500

# #DELETE 
# @app.route('/delete/telefonos_clientes/<int:id_cliente>/', methods=['POST'])
# def handle_delete(id_cliente):
#     try:
#         # Call your Python function here
#         eliminar_cliente_logico(id_cliente)
        
#         # Return success response to JavaScript
#         return jsonify({'success': True, 'message': 'Cliente eliminado correctamente'})
#     except Exception as e:
#         # Return failure response with error details to JavaScript
#         return jsonify({'success': False, 'message': str(e)}), 500
   


# ---------------- Correos de clientes (vista para Admin/Empleado) ----------------
# ---------------- Correos de clientes (vista para Admin/Empleado) ----------------
# ---------------- Correos de clientes (vista para Admin/Empleado) ----------------
@app.route('/correos_clientes')
def correos_clientes():
    datos_correos = obtener_correos_clientes()    
    return render_template('seccion_clientes/correos_clientes.html', correos=datos_correos)

@app.route("/api/correos_clientes/guardar", methods=["POST"])
def api_guardar_correo_cliente():
    datos = request.get_json()
    try:
        insertar_correos_clientes(
            ID_CLIENTE=datos["id_cliente"],
            CORREO=datos["correo"],
            TIPO=datos["tipo"],
            ID_ESTADO=datos["id_estado"]
        )
        return jsonify({"message": "¡Correo agregado con éxito en Oracle!"}), 200
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
        return jsonify({"message": "¡Correo actualizado con éxito en Oracle!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500

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
        return jsonify({"message": "¡Dirección agregada con éxito en Oracle!"}), 200
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
        return jsonify({"message": "¡Dirección actualizada con éxito en Oracle!"}), 200
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


@app.route("/api/puestos/guardar", methods=["POST"])
def api_guardar_puesto():
    datos = request.get_json()
    try:
        insertar_puesto(
            id_puesto=datos["id_puesto"],
            nombre=datos["nombre"],
            descripcion=datos["descripcion"]
        )
        return jsonify({"message": "¡Puesto agregado con éxito en Oracle!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al guardar en Base de Datos: {str(e)}"}), 500


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


@app.route("/api/puestos/eliminar/<int:id_puesto>", methods=["POST"])
def api_eliminar_puesto(id_puesto):
    try:
        eliminar_puesto_logico(id_puesto)
        return jsonify({"message": "¡Puesto eliminado con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al eliminar en Base de Datos: {str(e)}"}), 500

# ---------------- Empleados (vista para Admin/HHRR) ----------------
# ---------------- Empleados (vista para Admin/HHRR) ----------------
# ---------------- Empleados (vista para Admin/HHRR) ----------------
@app.route("/empleados")
def empleados():
    id_estado = request.args.get("estado")  # "1"=Activo, "2"=Inactivo, vacío=Todos
    lista_empleados = obtener_empleados()
    lista_puestos = obtener_puestos()
    return render_template("seccion_HR-SEC/empleados.html", empleados=lista_empleados, filtro=id_estado, puestos=lista_puestos)


@app.route("/api/empleados/guardar", methods=["POST"])
def api_guardar_empleado():
    datos = request.get_json()
    try:
        insertar_empleados(
            id_empleado=datos["id_empleado"],
            nombre=datos["nombre"],
            apellido_paterno=datos["apellido_paterno"],
            apellido_materno=datos["apellido_materno"],
            id_puesto=datos["id_puesto"],
            id_estado = 1
        )
        return jsonify({"message": "¡Empleado agregado con éxito en Oracle!"}), 200
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
        return jsonify({"message": "¡Empleado actualizado con éxito en Oracle!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500
    

@app.route("/delete/empleados/<int:id_empleado>", methods=["POST"])
def desactivar_empleado(id_empleado):
    try:
        eliminar_empleados_logica(id_empleado)
        return jsonify({'success': True, 'message': '¡Empleado desactivado con éxito!'}), 200
    except Exception as e:
        return jsonify({'success': False, 'message': f"Error al desactivar en Base de Datos: {str(e)}"}), 500

# ---------------- Correos Empleados (vista para Admin/HHRR) ----------------
# ---------------- Correos Empleados (vista para Admin/HHRR) ----------------
# ---------------- Correos Empleados (vista para Admin/HHRR) ----------------
@app.route('/correos_empleados')
def correos_empleados():
    datos_correos = obtener_correos_empleados()    
    return render_template('seccion_HR-SEC/correos_empleados.html', correos=datos_correos)

@app.route("/api/correos_empleados/guardar", methods=["POST"])
def api_guardar_correo_empleado():
    datos = request.get_json()
    try:
        insertar_correo_empleado(
            ID_EMPLEADO=datos["id_empleado"],
            CORREO=datos["correo"],
            TIPO=datos["tipo"],
            ID_ESTADO=datos["id_estado"]
        )
        return jsonify({"message": "¡Correo agregado con éxito en Oracle!"}), 200
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
        return jsonify({"message": "¡Correo actualizado con éxito en Oracle!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500


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

@app.route("/api/productos/guardar", methods=["POST"])
def api_guardar_producto():
    datos = request.get_json()
    try:
        insertar_producto(
            id_producto=datos["id_producto"],
            nombre=datos["nombre"],
            descripcion=datos["descripcion"],
            precio=datos["precio"],
            unidades=datos["unidades"],
            id_estado=datos["id_estado"]
        )
        return jsonify({"message": "¡Producto agregado con éxito en Oracle!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al guardar en Base de Datos: {str(e)}"}), 500


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
        return jsonify({"message": "¡Producto actualizado con éxito en Oracle!"}), 200
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
        return jsonify({"message": "¡Relación agregada con éxito en Oracle!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al guardar en Base de Datos: {str(e)}"}), 500


@app.route("/api/productos-x-proveedor/eliminar/<int:id_proveedor>/<int:id_producto>", methods=["POST"])
def api_eliminar_producto_x_proveedor(id_proveedor, id_producto):
    try:
        eliminar_producto_x_proveedor_logico(id_producto, id_proveedor)
        return jsonify({"message": "¡Relación desactivada con éxito!"}), 200
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

# @app.route("/api/proveedores/guardar", methods=["POST"])
# def api_guardar_proveedor():
#     datos = request.get_json()
#     try:
#         insertar_proveedor(
#             id_proveedor=datos["id_proveedor"],
#             nombre=datos["nombre"],
#             id_reabastecimiento=datos.get("id_reabastecimiento"),
#             id_estado= 1
#         )
#         return jsonify({"message": "¡Proveedor agregado con éxito en Oracle!"}), 200
#     except Exception as e:
#         return jsonify({"message": f"Error al guardar en Base de Datos: {str(e)}"}), 500

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

@app.route("/api/proveedores/eliminar/<int:id_proveedor>", methods=["POST"])
def api_eliminar_proveedor(id_proveedor):
    try:
        eliminar_proveedor_logico(id_proveedor)
        return jsonify({"message": "¡Proveedor desactivado con éxito!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al eliminar en Base de Datos: {str(e)}"}), 500


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
        return jsonify({"message": "¡Proveedor agregado con éxito en Oracle!"}), 200
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
    return render_template('seccion_inventario/correos_proveedores.html', correos=datos_correos)

@app.route("/api/correos_proveedores/guardar", methods=["POST"])
def api_guardar_correo_proveedor():
    datos = request.get_json()
    try:
        insertar_correo_proveedor(
            ID_PROVEEDOR=datos["id_proveedor"],
            CORREO=datos["correo"],
            TIPO=datos["tipo"],
            ID_ESTADO=datos["id_estado"]
        )
        return jsonify({"message": "¡Correo agregado con éxito en Oracle!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al guardar en Base de Datos: {str(e)}"}), 500

@app.route("/api/correos_proveedores/actualizar", methods=["POST"])
def api_actualizar_correo_proveedor():
    datos = request.get_json()
    try:
        actualizar_correo_proveedor(
            ID_PROVEEDOR=datos["id_proveedor"],
            CORREO=datos["correo"],
            TIPO=datos["tipo"],
            ID_ESTADO=datos["id_estado"]
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

# ---------------- Servicios (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Servicios (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Servicios (vista para Admin/Empleado/Cliente) ----------------
@app.route("/servicios")
def servicios():
    id_estado = request.args.get("estado")  # vacío = Todos, o el ID de cualquier estado del catálogo
    lista_servicios = obtener_servicios(id_estado)
    return render_template("seccion_operaciones/servicios.html", servicios=lista_servicios, filtro=id_estado)




# ---------------- Servicios Realizados (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Servicios Realizados (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Servicios Realizados (vista para Admin/Empleado/Cliente) ----------------
@app.route("/serviciosr")
def serviciosr():
    id_estado = request.args.get("estado")  # vacío = Todos, o el ID de cualquier estado del catálogo
    lista_servicios_realizados = obtener_servicios_realizados(id_estado)
    lista_estados = obtener_estados()
    return render_template("seccion_operaciones/serviciosr.html", serviciosr=lista_servicios_realizados, filtro=id_estado, estados=lista_estados)


@app.route("/api/serviciosr/guardar", methods=["POST"])
def api_guardar_servicio_realizado():
    datos = request.get_json()
    try:
        insertar_servicio_realizado(
            id_servicio_realizado=datos["id_servicio_realizado"],
            ubicacion=datos["ubicacion"],
            informe=datos["informe"],
            id_estado=datos["id_estado"]
        )
        return jsonify({"message": "¡Servicio registrado con éxito en Oracle!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al guardar en Base de Datos: {str(e)}"}), 500


@app.route("/api/serviciosr/actualizar", methods=["POST"])
def api_actualizar_servicio_realizado():
    datos = request.get_json()
    try:
        actualizar_servicio_realizado(
            id_servicio_realizado=datos["id_servicio_realizado"],
            ubicacion=datos["ubicacion"],
            informe=datos["informe"],
            id_estado=datos["id_estado"]
        )
        return jsonify({"message": "¡Servicio actualizado con éxito en Oracle!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error al actualizar en Base de Datos: {str(e)}"}), 500

# ---------------- Visitas (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Visitas (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Visitas (vista para Admin/Empleado/Cliente) ----------------
@app.route("/visitas")
def visitas():
    lista_visitas = obtener_visitas()
    return render_template("seccion_operaciones/visitas.html", visitas=lista_visitas)

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
            id_provincia=datos["id_provincia"],
            nombre=datos["nombre"],
            id_estado=datos["id_estado"]
        )
        return jsonify({'success': True,"message": "¡Provincia agregada con éxito en Oracle!"}), 200
    except Exception as e:
        return jsonify({'success': False, "message": f"Error al guardar en Base de Datos: {str(e)}"}), 500

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
            id_canton=datos["id_canton"],
            nombre=datos["nombre"],
            id_estado=datos["id_estado"]
        )
        return jsonify({'success': True,"message": "¡Canton agregado con éxito en Oracle!"}), 200
    except Exception as e:
        return jsonify({'success': False, "message": f"Error al guardar en Base de Datos: {str(e)}"}), 500

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
            id_distrito=datos["id_distrito"],
            nombre=datos["nombre"],
            id_estado=datos["id_estado"]
        )
        return jsonify({'success': True,"message": "¡Distrito agregado con éxito en Oracle!"}), 200
    except Exception as e:
        return jsonify({'success': False, "message": f"Error al guardar en Base de Datos: {str(e)}"}), 500






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
    return render_template("seccion_fyf/metodos_pago.html", metodos=lista_metodos)

# ---------------- Pagos (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Pagos (vista para Admin/Empleado/Cliente) ----------------
# ---------------- Pagos (vista para Admin/Empleado/Cliente) ----------------
@app.route("/pagos")
def pagos():
    lista_pagos = obtener_pagos()
    return render_template("seccion_fyf/pagos.html", pagos=lista_pagos)

@app.route("/api/pagos/guardar", methods=["POST"])
def api_guardar_pago():
    datos = request.get_json()
    try:
        insertar_pago(
            id_pago=datos["id_pago"],
            nombre=datos["nombre"],
            id_reabastecimiento=datos.get("id_reabastecimiento"),
            id_estado= 1
        )
        return jsonify({"message": "¡Pago agregado con éxito en Oracle!"}), 200
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
        return jsonify({"message": "¡Transacción agregada con éxito en Oracle!"}), 200
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
    return render_template("seccion_fyf/detalle_transacciones.html", detalle=lista_detalle)

@app.route("/api/proveedores/guardar", methods=["POST"])
def api_guardar_proveedor():
    datos = request.get_json()
    try:
        insertar_proveedor(
            id_proveedor=datos["id_proveedor"],
            nombre=datos["nombre"],
            id_reabastecimiento=datos.get("id_reabastecimiento"),
            id_estado= 1
        )
        return jsonify({"message": "¡Proveedor agregado con éxito en Oracle!"}), 200
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


@app.route("/api/detalle_transacciones/eliminar/<int:id_detalle_transaccion>", methods=["POST"])
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
    plantilla = "seccion_fyf/facturas_billing.html" if session.get("rol") == "Billing" else "seccion_fyf/facturas_admin.html"
    return render_template(
        plantilla,
        facturas=facturas,
        clientes=clientes,
        id_cliente_seleccionado=id_cliente,
    )


MESES_NOMBRE = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
    7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre",
}


@app.route("/reporte-ventas")
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


DIAS_AVISO_RENOVACION = 7


@app.route("/suscripciones-activas")
def suscripciones_activas():
    suscripciones = obtener_suscripciones_activas()
    ahora = datetime.now()
    for s in suscripciones:
        fecha = s.get("FECHA_PROXIMA_RENOVACION")
        dias_restantes = (fecha - ahora).days if fecha else None
        s["dias_restantes"] = dias_restantes
        s["por_vencer"] = dias_restantes is not None and 0 <= dias_restantes <= DIAS_AVISO_RENOVACION
    return render_template("seccion_fyf/suscripciones_activas.html", suscripciones=suscripciones)


###########################################################################################
################################## SECCION - OTROS ##################################
###########################################################################################
# ---------------- OLVIDE PASSWORD (vista para Admin/Empleado/Cliente) ----------------
# ---------------- OLVIDE PASSWORD (vista para Admin/Empleado/Cliente) ----------------
# ---------------- OLVIDE PASSWORD (vista para Admin/Empleado/Cliente) ----------------
@app.route("/olvide-password")
def olvide_password():
    return render_template("olvide_password.html")

# Ruta que recibe la petición Fetch del JavaScript
@app.route('/olvide-password/reset', methods=['POST'])
def reset_password():
    try:
        data = request.get_json()
        user_email = data.get('email')

        if not user_email:
            return jsonify({'success': False, 'error': 'El correo es requerido.'}), 400
        
        else:              
            # Llama a la función que está dentro de olvide_password.py
            get_usuario_id(user_email)

            return jsonify({
                'success': True, 
                'message': 'Nueva contraseña enviada con éxito.'
            }), 200

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400




@app.before_request
def verificar_acceso():
    if request.path.startswith("/static") or request.path in ("/login", "/registro", "/olvide-password"):
        return
    if "id_usuario" not in session:
        return redirect(url_for("login"))

    rol = session.get("rol")

    if rol == "Cliente" and not request.path.startswith(RUTAS_CLIENTE):
        return redirect(url_for("inicio_cliente"))

    if rol == "RRHH" and not request.path.startswith(RUTAS_RRHH):
        return redirect(url_for("empleados"))

    if rol == "Billing" and not request.path.startswith(RUTAS_BILLING):
        return redirect(url_for("facturas_admin"))

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

@app.route("/mis-facturas")
def mis_facturas():
    facturas = obtener_facturas_cliente(session["id_cliente"])
    return render_template("mis_facturas.html", facturas=facturas)

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