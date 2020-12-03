ventana = new Ventana();

function Ventana(){
	var datos="";
    this.showHTML = function (objContainer,stPagina){
           $.ajax({
                  type: "GET",
                  url: stPagina ,
                  async: false,
                  cache: false,

                  success: function (response) {
                        datos = response;
                    },
                  error: function (msg, status, errorThrown) {
                  	      alert (msg)
                            datos = "Error " + msg
                            datos=null;
                  }
            });
        document.getElementById(objContainer).innerHTML = datos;
    }
    this.getPostData = function (stPagina, stData){
           $.ajax({
                  type: "POST",
                  url: stPagina ,
                  async: false,
                  cache: false,
                  data : stData,

                  dataType : 'json',
                  success: function (response) {
                        datos = response;
                    },
                  error: function (msg, status, errorThrown) {
                          alert (msg)
                            datos = "Error " + msg

                            datos=null;
                  }
            });

        return datos;
    }
    this.getPostHtml = function (objContainer,stPagina,stData){
        $.ajax({
            type: "POST",
            url: stPagina ,
            async: false,
            cache: false,
            data: stData,
            success: function (response) {
                    datos = response;
                },
            error: function (msg, status, errorThrown) {
                    alert (msg)
                    datos = "Error " + msg
                    datos=null;
            }
         });
        document.getElementById(objContainer).innerHTML = datos;
    }
}
