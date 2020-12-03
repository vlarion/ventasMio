mpProducto = new listaProd();
function listaProd(){

    function verLocal(){
        }

    this.Ver = function(){
        var stData = "Codigo=" + document.getElementById("txCodigo").value
        var reg=ventana.getPostData("productoLeer", stData)
        //llamado de datos
        document.getElementById("txImagen").value=reg[0].fields.imgProducto;
        document.getElementById("txNombre").value=reg[0].fields.nombreProd;
        document.getElementById("txPrecio").value=reg[0].fields.precio;
        document.getElementById("txEstado").value=reg[0].fields.estado;
        document.getElementById("txGarantia").value=reg[0].fields.garantia;
        document.getElementById("txCantidad").value=reg[0].fields.cantidad;
        document.getElementById("txFicha").value=reg[0].fields.fichaTecnica;
        document.getElementById("txDescrip").value=reg[0].fields.descripcion;
        document.getElementById("cbProveedor").value=reg[0].fields.idProv;
        document.getElementById("cbMarca").value=reg[0].fields.idMarca;
        document.getElementById("cbModelo").value=reg[0].fields.idModelo;
        
        
        /* estado de los botones*/
        document.getElementById("btVer").disabled = true;
        document.getElementById("btActualizar").disabled = false;
        document.getElementById("btCrear").disabled = false;
        document.getElementById("btEliminar").disabled = false;
        document.getElementById("btCancelar").disabled = false;

        /* estado de los datos*/
        document.getElementById("txImagen").disabled = false;
        document.getElementById("txCodigo").disabled = true;
        document.getElementById("txNombre").disabled = false;
        document.getElementById("txPrecio").disabled = false;
        document.getElementById("txEstado").disabled = false;
        document.getElementById("txGarantia").disabled = false;
        document.getElementById("txCantidad").disabled = false;
        document.getElementById("txFicha").disabled = false;
        document.getElementById("txDescrip").disabled = false;
        document.getElementById("cbProveedor").disabled = false;
        document.getElementById("cbMarca").disabled = false;
        document.getElementById("cbModelo").disabled = false;
        }

    this.Actualizar = function(){
        alert("Está seguro de actualizar este producto???")
        var stData= "Codigo=" + document.getElementById("txCodigo").value
               + "&Nombre=" + document.getElementById("txNombre").value
               + "&Precio=" + document.getElementById("txPrecio").value
               + "&Estado=" + document.getElementById("txEstado").value
               + "&Garantia=" + document.getElementById("txGarantia").value
               + "&Cantidad=" + document.getElementById("txCantidad").value
               + "&Ficha=" + document.getElementById("txFicha").value
               + "&Descripcion=" + document.getElementById("txDescrip").value
               + "&ImgProducto=" + document.getElementById("txImagen").value
               + "&Marca" + document.getElementById("cbMarca").value
               + "&Modelo" + document.getElementById("cbModelo").value
               + "&Proveedor" + document.getElementById("cbProveedor").value
        var reg=ventana.getPostData("productoActualizar", stData)
        alert("registro " +reg)
        if (reg.ok){
            alert(reg.msg)
            return
            }
        alert("error,"+ reg.msg)
        }

    

    this.Eliminar = function(){        
        var stData = "Codigo=" + document.getElementById("txCodigo").value
        var reg=ventana.getPostData("productoEliminar", stData)
        alert("eliminando"+reg)
        if (reg.ok){
            alert(reg.msg)
            return
        }
        alert("error,"+ reg.msg)
        }

    this.Cancelar = function(){

        /* estado de los botones*/
        document.getElementById("btVer").disabled = true;
        document.getElementById("btActualizar").disabled = true;
        document.getElementById("btCrear").disabled = false;
        document.getElementById("btEliminar").disabled = true;
        document.getElementById("btCancelar").disabled = true;

        /* estado de los datos*/
        document.getElementById("txCodigo").disabled = false;
        document.getElementById("txNombre").disabled = true;
        document.getElementById("txPrecio").disabled = true;
        document.getElementById("txEstado").disabled = true;
        document.getElementById("txGarantia").disabled = true;
        document.getElementById("txCantidad").disabled = true;
        document.getElementById("txFicha").disabled = true;
        document.getElementById("txDescrip").disabled = true;
        document.getElementById("txImagen").disabled = true;
        document.getElementById("cbMarca").disabled = true;
        document.getElementById("cbModelo").disabled = true;
        document.getElementById("cbProveedor").disabled = true;

        document.getElementById("txCodigo").value = "";
        document.getElementById("txNombre").value = "";
        document.getElementById("txPrecio").value = "";
        document.getElementById("txEstado").value = "";
        document.getElementById("txGarantia").value = "";
        document.getElementById("txCantidad").value = "";
        document.getElementById("txFicha").value = "";
        document.getElementById("txDescrip").value = "";
        document.getElementById("txImagen").value = "";
        document.getElementById("cbMarca").value = "";
        document.getElementById("cbModelo").value = "";
        document.getElementById("cbProveedor").value = "";

        document.getElementById("btVer").disabled = false;
        }

    this.editar= function(Codigo){
        var stDatos = "idProducto="+Codigo
        ventana.getPostHtml("containerRight","prodListado/",stDatos)
        /* estado de los datos*/
        document.getElementById("txCodigo").disabled = true;
        document.getElementById("txNombre").disabled = false;
        document.getElementById("txPrecio").disabled = false;
        document.getElementById("txEstado").disabled = false;
        document.getElementById("txGarantia").disabled = false;
        document.getElementById("txCantidad").disabled = false;
        document.getElementById("txFicha").disabled = false;
        document.getElementById("txDescrip").disabled = false;
        document.getElementById("txImagen").disabled = false;
        document.getElementById("cbMarca").disabled = false;
        document.getElementById("cbModelo").disabled = false;
        document.getElementById("cbProveedor").disabled = false;
        document.getElementById("btActualizar").disabled = false;
    }

    this.Leer = function(){
        var stDato = "Codigo=" + document.getElementById("txCodigo").value      
        reg=ventana.getPostHtml("containerRight","prodList/", stDato)
        try{
            if (reg.length == 0){
                document.getElementById("btVer").disabled = true;
                document.getElementById("btEliminar").disabled = true;
                document.getElementById("btActualizar").innerText = "Guardar";           
                
            }
            else {
                document.getElementById("txNombre").value=reg[0].fields.nombreProd;     
                document.getElementById("txPrecio").value=reg[0].fields.precio;     
                document.getElementById("txEstado").value=reg[0].fields.estado;   
                document.getElementById("txGarantia").value=reg[0].fields.garantia;
                document.getElementById("txCantidad").value=reg[0].fields.cantidad; 
                document.getElementById("txFicha").value=reg[0].fields.fichaTecnica; 
                document.getElementById("txDescrip").value=reg[0].fields.descripcion;
                document.getElementById("txImagen").value=reg[0].fields.imgProducto;
                document.getElementById("cbProveedor").value=reg[0].fields.idProv;
                document.getElementById("btActualizar").innerText = "Actualizar";
            }
        }catch{
		document.getElementById("btCancelar").disabled = false;
        document.getElementById("btActualizar").disabled = false;
        document.getElementById("txCodigo").disabled = true;
		document.getElementById("txNombre").disabled = false;
		document.getElementById("txPrecio").disabled = false;		 
		document.getElementById("txEstado").disabled = false;		 
        document.getElementById("txGarantia").disabled = false;	 
        document.getElementById("txCantidad").disabled = false;
        document.getElementById("txFicha").disabled = false;
        document.getElementById("txDescrip").disabled = false;
        document.getElementById("txImagen").disabled = false;
		document.getElementById("cbProveedor").disabled = false;		 
		document.getElementById("cbMarca").disabled = false;		 
        document.getElementById("cbModelo").disabled = false;		
        document.getElementById("btEliminar").disabled = false; 
        }
    }

    this.Crear = function(){

        /* estado de los datos*/
        document.getElementById("txCodigo").disabled = false;
        document.getElementById("txNombre").disabled = false;
        document.getElementById("txPrecio").disabled = false;
        document.getElementById("txEstado").disabled = false;
        document.getElementById("txGarantia").disabled = false;
        document.getElementById("txCantidad").disabled = false;
        document.getElementById("txFicha").disabled = false;
        document.getElementById("txDescrip").disabled = false;
        document.getElementById("txImagen").disabled = false;
        document.getElementById("cbProveedor").disabled = false;
        document.getElementById("cbMarca").disabled = false;
        document.getElementById("cbModelo").disabled = false;
        document.getElementById("btActualizar").disabled = false;
        document.getElementById("btActualizar").innerText = "Guardar";
        
        var stData= "Codigo=" + document.getElementById("txCodigo").value
               + "&Nombre=" + document.getElementById("txNombre").value
               + "&Precio=" + document.getElementById("txPrecio").value
               + "&Estado=" + document.getElementById("txEstado").value
               + "&Garantia=" + document.getElementById("txGarantia").value
               + "&Cantidad=" + document.getElementById("txCantidad").value
               + "&Ficha=" + document.getElementById("txFicha").value
               + "&Descripcion=" + document.getElementById("txDescrip").value
               + "&imgProducto=" + document.getElementById("txImagen").value
               + "&Marca" + document.getElementById("cbMarca").value
               + "&Modelo" + document.getElementById("cbModelo").value
               + "&Proveedor" + document.getElementById("cbProveedor").value

        var reg=ventana.getPostData("productoCrear", stData)
        if (reg.ok){
            alert(reg.msg)
            return
            }
        alert("error,"+ reg.msg)
        }

        this.Listar = function(){
            ventana.showHTML('containerRight','productoListado')
            }
        
        this.Lista = function(){
            ventana.showHTML('containerRight','producto')
            }

        this.Image = function(){
            ventana.showHTML('containerRight','imagen')
            }

}