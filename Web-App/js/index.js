//console.log ("Conexion js Link")
//<!----- Script 1------>
//<!-- Get all paises -->
//<script>
    //fetch('http://181.199.66.129:5010/pais')
    fetch('http://181.199.66.129:5010/Test')
    .then(ListTest=>ListTest.json())
    .then(ListTest=>{
      //console.log("Test")
        //console.log(ListTest)
        
        var resultado = document.getElementById('Test');
        var n = 0;
        Test.innerHTML = '';
        Test.innerHTML = '<option selected="Test">Test Numero</option>';
        
        for(let dato of ListTest){
            n++;
            resultado.innerHTML += `
            <option value="${dato.Id}"> (${dato.Id}) - ${dato.GUID}</option>
            
            `;
           
        }
       
    })
    
//</script>

/*
//<!----- Script 2------>
//<!-- get provincia Segun opcion seleccionada en el drowndoon-->
//<script>	  
	$(document).ready(function(){
    $("#Test").on("change",function(){						
      var Testnumero =$(this).val()//obtenemos el valor seleccionado en una variable	
      //console.log("Test Seleccionado: " + Testnumero) 

  fetch('http://181.199.66.129:5010/ciclo/'+Testnumero+'')
  

	.then(Listciclos=>Listciclos.json())
	.then(Listciclos=>{
  //console.log("Ciclos")   
  //console.log( Listciclos)
  
    var resultado = document.getElementById('Ciclo');
        var n = 0;

        
        Ciclo.innerHTML = '<option selected="Ciclo" >Ciclo</option>';
        
        for(let dato of Listciclos){
            n++;
            resultado.innerHTML += `
            <option value="${dato.CicloTest}">Cliclo: ${dato.CicloTest}</option>
            
            `;
			}
			
			})
		})
	})
//</script>
*/

//<!----- Script 3------>
//<!-- get provincia Segun opcion seleccionada en el drowndoon-->
//<script>	  
$(document).ready(function(){
  $("#Test").on("change",function(){						
    var Testnumero =$(this).val()//obtenemos el valor seleccionado en una variable	
    console.log("Test Seleccionado: " + Testnumero) 

	$(document).ready(function(){
    $("#Ciclo").on("change",function(){						
      var CicloSelectd=$(this).val()//obtenemos el valor seleccionado en una variable	
      console.log("Ciclo Seleccionado: " + CicloSelectd) 
			
   fetch('http://181.199.66.129:5010/Resultado/'+Testnumero+'/'+CicloSelectd+'')

	.then(datos=>datos.json())
	.then(datos=>{
  console.log("Resultado")   
  console.log( datos)
  
    
      
  contenido.innerHTML = '';
        
        n = 0
        for(let dato of datos){
            n++;
            contenido.innerHTML += `
            <tr>
                    <th scope="row">${ n }</th>
                    <td>${ dato.Name }</td>
                    <td>${ dato.Total }</td>
                    <td>${ dato.Total }</td>
                    <td>${ dato.Total }</td>
                    <td>${ dato.Total }</td>
                    <td></td>
                </tr>
                
            
            `;
			}
			
			})
		})
  })
})})
  
// </script>



//<!----- Script 3------>
//<!-- get provincia Segun opcion seleccionada en el drowndoon-->
//<script>	  
$(document).ready(function(){
  $("#Test").on("change",function(){						
    var Testnumero =$(this).val()//obtenemos el valor seleccionado en una variable	
    //console.log("Test Seleccionado: " + Testnumero) 

   fetch('http://181.199.66.129:5010/Testnumero/'+Testnumero+'/1')

	.then(datos=>datos.json())
	.then(datos=>{
  console.log("Resultado")   
  console.log( datos)
  
    
      
  contenido.innerHTML = '';
        
        n = 0
        for(let dato of datos){
            n++;
            contenido.innerHTML += `
            <tr>
                    <th scope="row">${ n }</th>
                    <td>${ dato.Name }</td>
                    <td>${ dato.Total }</td>
                    <td>--</td>
                    <td>--</td>
                    <td>--</td>

                </tr>
                
            
            `;
			}
			
			})
		})
  })

  
// </script>


//<!----- Script 3------>
//<!-- get provincia Segun opcion seleccionada en el drowndoon-->
//<script>	  
$(document).ready(function(){
  $("#Test").on("change",function(){						
    var Testnumero =$(this).val()//obtenemos el valor seleccionado en una variable	
    //console.log("Test Seleccionado: " + Testnumero) 

   fetch('http://181.199.66.129:5010/Testnumero/'+Testnumero+'/2')

	.then(datos=>datos.json())
	.then(datos=>{
  console.log("Resultado")   
  console.log( datos)
  
    
      
  contenido2.innerHTML = '';
        
        n = 0
        for(let dato of datos){
            n++;
            contenido2.innerHTML += `
            <tr>
                    <th scope="row">${ n }</th>
                    <td>${ dato.Name }</td>
                    <td>${ dato.Total }</td>
                    <td>--</td>
                    <td>--</td>
                    <td>--</td>
                </tr>
                
            
            `;
			}
			
			})
		})
  })

  
// </script>


//<!----- Script 3------>
//<!-- get provincia Segun opcion seleccionada en el drowndoon-->
//<script>	  
$(document).ready(function(){
  $("#Test").on("change",function(){						
    var Testnumero =$(this).val()//obtenemos el valor seleccionado en una variable	
    //console.log("Test Seleccionado: " + Testnumero) 

   fetch('http://181.199.66.129:5010/Testnumero/'+Testnumero+'/3')

	.then(datos=>datos.json())
	.then(datos=>{
  console.log("Resultado")   
  console.log( datos)
  
    
      
  contenido3.innerHTML = '';
        
        n = 0
        for(let dato of datos){
            n++;
            contenido3.innerHTML += `
            <tr>
                    <th scope="row">${ n }</th>
                    <td>${ dato.Name }</td>
                    <td>${ dato.Total }</td>
                    <td>--</td>
                    <td>--</td>
                    <td>--</td>
                
            
            `;
			}
			
			})
		})
  })

  
// </script>


//<!----- Script 3------>
//<!-- get provincia Segun opcion seleccionada en el drowndoon-->
//<script>	  
$(document).ready(function(){
  $("#Test").on("change",function(){						
    var Testnumero =$(this).val()//obtenemos el valor seleccionado en una variable	
    //console.log("Test Seleccionado: " + Testnumero) 

   fetch('http://181.199.66.129:5010/Testnumero/'+Testnumero+'/4')

	.then(datos=>datos.json())
	.then(datos=>{
  console.log("Resultado")   
  console.log( datos)
  
    
      
  contenido4.innerHTML = '';
        
        n = 0
        for(let dato of datos){
            n++;
            contenido4.innerHTML += `
            <tr>
                    <th scope="row">${ n }</th>
                    <td>${ dato.Name }</td>
                    <td>${ dato.Total }</td>
                    
                    <td>--</td>
                    <td>--</td>
                    <td>--</td>
                </tr>
                
            
            `;
			}
			
			})
		})
  })

  
// </script>



//<!----- Script 3------>
//<!-- get provincia Segun opcion seleccionada en el drowndoon-->
//<script>	  
$(document).ready(function(){
  $("#Test").on("change",function(){						
    var Testnumero =$(this).val()//obtenemos el valor seleccionado en una variable	
    //console.log("Test Seleccionado: " + Testnumero) 

   fetch('http://181.199.66.129:5010/DetailTest/'+Testnumero)

	.then(datos=>datos.json())
	.then(datos=>{
  console.log("Resultado")   
  console.log( datos)
  
    
  Fecha.innerHTML = '';
  TestNumero.innerHTML = '';
  HostName.innerHTML = '';
  Resultado.innerHTML = '';
  TCiclos.innerHTML = '';
  DCiclo.innerHTML = '';
  Descripcion.innerHTML = '';
  Recurso.innerHTML = '';
        

  Fecha.innerHTML += `${ datos[0].Fecha }`;
  TestNumero.innerHTML += `${ datos[0].GUID }`;
  HostName.innerHTML += `${ datos[0].Hostname }`;
  Resultado.innerHTML += `${ datos[0].Resultado }`;
  TCiclos.innerHTML += `${ datos[0].TotalCiclos }`;
  DCiclo.innerHTML += `${ datos[0].Duracion } Segundos` ;
  Descripcion.innerHTML += `${ datos[0].Descripcion }`;
  Recurso.innerHTML += `<a href="${ datos[0].Recurso }">${ datos[0].Recurso }`;

			
			})
		})
  })

  
// </script>