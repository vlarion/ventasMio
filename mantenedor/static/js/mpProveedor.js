mpProveedor = new proveedor();
function proveedor(){

    this.loadCombo = function(stIdProveedor){
		var stDatos = "idProv=" + stIdProveedor
		ventana.getPostHtml("selProveedor","proveedorCombo/",stDatos)		
	}

   
}