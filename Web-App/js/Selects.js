//console.log ("Conexion js Link")
//<!----- Script 1------>
//<!-- Get all paises -->
//<script>
    //fetch('http://181.199.66.129:5010/pais')
    fetch('http://192.168.100.51:5080/Test')
    .then(ListTest=>ListTest.json())
    .then(ListTest=>{
      console.log("Test-----------")
        console.log(ListTest)
        
        var resultado = document.getElementById('Test');
        var n = 0;
        Test.innerHTML = '';
        Test.innerHTML = '<option selected="Test">Test Numero</option>';
        
        for(let dato of ListTest){
            n++;
            resultado.innerHTML += `
            <option value="${dato.Id}"> (${dato.Id}) - ${dato.GUID} - ${dato.CameraMode} Camera - ${dato.iServices} </option>
            
            `;
           
        }
       
    })
    
//</script>


//<!----- Script 3------>
//<!-- Resumen ciclo 1-->
//<script>	  

$(document).ready(function(){
  $("#Test").on("change",function(){						
    var Testnumero =$(this).val()//obtenemos el valor seleccionado en una variable	
    //console.log("Test Seleccionado: " + Testnumero) 

   fetch('http://192.168.100.51:5080/ResumenCiclo/'+Testnumero+'')

	.then(datos=>datos.json())
	.then(datos=>{
  console.log("Resultado resumen ciclo")   
  console.log( datos)
  
    
      
  ResumenCiclo.innerHTML = '';
        
        n = 0
        for(let dato of datos){
            n++;
            ResumenCiclo.innerHTML += `
            <tr>
                    <th scope="row">${ n }</th>
                    
                    <td>${ dato.Ciclo }</td>
                    <td>${ dato.TotalIdentificacion }</td>
                    <td>${ dato.TotalFrameReceived }</td>
                    <td>${ dato.TotalBeforeProcessing }</td>
                    <td>${ dato.TotalFrameReceived - dato.TotalBeforeProcessing }</td>
                    <td>${ dato.LocalPhotos }</td>
                    <td>${ dato.AfterIdentification }</td>
                              
                    <td>${ dato.CpuAve } %</td>
                    <td>${ dato.RamAve } MB</td>
                    <td>${ dato.TotalError }</td>
                    <td>${ dato.TotalFileMetrics }</td>
                    <td>${ dato.TotalFileMetricsIdentification }</td>
                    <td>${ dato.TotalFIleSinPersonEngagements }</td>
                </tr>
                
            
            `;
			}
			
			})
		})
  })

  
// </script>


//<!----- Script 3------>
//<!-- Frame sumari
//<script>	  
$(document).ready(function(){
  $("#Test").on("change",function(){						
    var Testnumero =$(this).val()//obtenemos el valor seleccionado en una variable	
    //console.log("Test Seleccionado: " + Testnumero) 

   fetch('http://192.168.100.51:5080/FrameSummary/'+Testnumero+'/1')

	.then(datos=>datos.json())
	.then(datos=>{
  console.log("Resultado resumen FrameSummary 2")   
  console.log( datos)
  
    
      
  FrameSummary.innerHTML = '';
        
        n = 0
        for(let dato of datos){
            n++;
            FrameSummary.innerHTML += `
            <tr>
                    <th scope="row">${ n }</th>
                    
                    <td>${ dato.Ciclo }</td>
                    <td>${ dato.Folder }</td>
                    <td>${ dato.Cam1 }</td>
                    <td>${ dato.Cam2 }</td>
                    <td>${ dato.Cam3 }</td>
					<td>${ dato.Cam4 }</td>
					<td>${ dato.CountFrame }</td>
                    
					
                
            
            `;
			}
			
			})
		})
  })

  
// </script>





//<!----- Script 3------>
//<!-- Frame sumari
//<script>	  
$(document).ready(function(){
  $("#Test").on("change",function(){						
    var Testnumero =$(this).val()//obtenemos el valor seleccionado en una variable	
    //console.log("Test Seleccionado: " + Testnumero) 

   fetch('http://192.168.100.51:5080/FrameSummary/'+Testnumero+'/2')

	.then(datos=>datos.json())
	.then(datos=>{
  console.log("Resultado resumen FrameSummary 2")   
  console.log( datos)
  
    
      
  FrameSummary2.innerHTML = '';
        
        n = 0
        for(let dato of datos){
            n++;
            FrameSummary2.innerHTML += `
            <tr>
                    <th scope="row">${ n }</th>
                    
                    <td>${ dato.Ciclo }</td>
                    <td>${ dato.Folder }</td>
                    <td>${ dato.Cam1 }</td>
                    <td>${ dato.Cam2 }</td>
                    <td>${ dato.Cam3 }</td>
					<td>${ dato.Cam4 }</td>
					<td>${ dato.CountFrame }</td>
                    
					
                
            
            `;
			}
			
			})
		})
  })

  
// </script>



//<!----- Script 3------>
//<!-- Frame sumari
//<script>	  
$(document).ready(function(){
  $("#Test").on("change",function(){						
    var Testnumero =$(this).val()//obtenemos el valor seleccionado en una variable	
    //console.log("Test Seleccionado: " + Testnumero) 

   fetch('http://192.168.100.51:5080/FrameSummary/'+Testnumero+'/3')

	.then(datos=>datos.json())
	.then(datos=>{
  console.log("Resultado resumen FrameSummary 3")   
  console.log( datos)
  
    
      
  FrameSummary3.innerHTML = '';
        
        n = 0
        for(let dato of datos){
            n++;
            FrameSummary3.innerHTML += `
            <tr>
                    <th scope="row">${ n }</th>
                    
                    <td>${ dato.Ciclo }</td>
                    <td>${ dato.Folder }</td>
                    <td>${ dato.Cam1 }</td>
                    <td>${ dato.Cam2 }</td>
                    <td>${ dato.Cam3 }</td>
					<td>${ dato.Cam4 }</td>
					<td>${ dato.CountFrame }</td>
                    
					
                
            
            `;
			}
			
			})
		})
  })

  
// </script>



//<!----- Script 3------>
//<!-- Frame sumari
//<script>	  
$(document).ready(function(){
  $("#Test").on("change",function(){						
    var Testnumero =$(this).val()//obtenemos el valor seleccionado en una variable	
    //console.log("Test Seleccionado: " + Testnumero) 

   fetch('http://192.168.100.51:5080/FrameSummary/'+Testnumero+'/4')

	.then(datos=>datos.json())
	.then(datos=>{
  console.log("Resultado resumen FrameSummary 4")   
  console.log( datos)
  
    
      
  FrameSummary4.innerHTML = '';
        
        n = 0
        for(let dato of datos){
            n++;
            FrameSummary4.innerHTML += `
            <tr>
                    <th scope="row">${ n }</th>
                    
                    <td>${ dato.Ciclo }</td>
                    <td>${ dato.Folder }</td>
                    <td>${ dato.Cam1 }</td>
                    <td>${ dato.Cam2 }</td>
                    <td>${ dato.Cam3 }</td>
					<td>${ dato.Cam4 }</td>
					<td>${ dato.CountFrame }</td>
                    
					
                
            
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
    console.log("Test Seleccionado: " + Testnumero) 

	$(document).ready(function(){
    $("#Ciclo").on("change",function(){						
      var CicloSelectd=$(this).val()//obtenemos el valor seleccionado en una variable	
      console.log("Ciclo Seleccionado: " + CicloSelectd) 
			
   fetch('http://192.168.100.51:5080/Resultado/'+Testnumero+'/'+CicloSelectd+'')

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

   fetch('http://192.168.100.51:5080/Testnumero/'+Testnumero+'/1')

	.then(datos=>datos.json())
	.then(datos=>{
  console.log("Resultado-------------")   
  console.log( datos)
  
    
      
  contenido.innerHTML = '';
        
        n = 0
        for(let dato of datos){
            n++;
            contenido.innerHTML += `
            <tr>
                    
            <th scope="row">${ n }</th>
            <td>${ dato.PersonId }</td>
            <td>${ dato.Name }</td>
            <td>${ dato.Total }</td>
            <td>${ dato.Minimo } %</td>
            <td>${ dato.Maximo } %</td>
            <td>${ dato.Average.toFixed(2)} %</td>

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

   fetch('http://192.168.100.51:5080/Testnumero/'+Testnumero+'/2')

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
            <td>${ dato.PersonId }</td>
            <td>${ dato.Name }</td>
            <td>${ dato.Total }</td>
            <td>${ dato.Minimo } %</td>
            <td>${ dato.Maximo } %</td>
            <td>${ dato.Average.toFixed(2)} %</td>
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

   fetch('http://192.168.100.51:5080/Testnumero/'+Testnumero+'/3')

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
            <td>${ dato.PersonId }</td>
            <td>${ dato.Name }</td>
            <td>${ dato.Total }</td>
            <td>${ dato.Minimo } %</td>
            <td>${ dato.Maximo } %</td>
            <td>${ dato.Average.toFixed(2)} %</td>
                    
                
            
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

   fetch('http://192.168.100.51:5080/Testnumero/'+Testnumero+'/4')

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
            <td>${ dato.PersonId }</td>
            <td>${ dato.Name }</td>
            <td>${ dato.Total }</td>
            <td>${ dato.Minimo } %</td>
            <td>${ dato.Maximo } %</td>
            <td>${ dato.Average.toFixed(2)} %</td>
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

   fetch('http://181.199.66.129:5080/DetailTest/'+Testnumero)

	.then(datos=>datos.json())
	.then(datos=>{
  console.log("Resultado")   
  console.log( datos)
  
    
  Fecha.innerHTML = '';
  TestNumero.innerHTML = '';
  HostName.innerHTML = '';
  CamarasConectadas.innerHTML = '';
  TCiclos.innerHTML = '';
  DCiclo.innerHTML = '';
  Descripcion.innerHTML = '';
  FaceAnalysisOptimization.innerHTML = '';
  Version.innerHTML = '';  
  Version2.innerHTML = '';   
  CameraMode.innerHTML = ''; 
  IdentificationService.innerHTML = ''; 
  BetweenPictures.innerHTML = ''; 
  

  Fecha.innerHTML += `${ datos[0].Fecha }`;
  TestNumero.innerHTML += `${ datos[0].GUID }`;
  HostName.innerHTML += `${ datos[0].Hostname }`;
  Version.innerHTML += `${ datos[0].VersionClient }`;
  Version2.innerHTML += `${ datos[0].VersionServices }`;
  IdentificationService.innerHTML += `${ datos[0].iServices } `;
  BetweenPictures.innerHTML += ` ${ datos[0].BetweenPictures } `;
  CameraMode.innerHTML += `${ datos[0].CameraMode }`;
  CamarasConectadas.innerHTML += `${ datos[0].TotalCamera}`;
  TCiclos.innerHTML += `${ datos[0].TotalCiclos }`;
  DCiclo.innerHTML += `${ datos[0].Duracion } Segundos` ;
  Descripcion.innerHTML += `${ datos[0].Descripcion }`;
  FaceAnalysisOptimization.innerHTML += `${ datos[0].FaceAnalysisOptimization }`;

			
			})
		})
  })

  
// </script>


//<!----- Script 3------>
//<!-- CAmera Summary-->
//<script>	  
$(document).ready(function(){
  $("#Test").on("change",function(){						
    var Testnumero =$(this).val()//obtenemos el valor seleccionado en una variable	
    //console.log("Test Seleccionado: " + Testnumero) 

   fetch('http://192.168.100.51:5080/CameraSummary/'+Testnumero+'')

	.then(datos=>datos.json())
	.then(datos=>{
  console.log("Resultado resumen Camera Summary")   
  console.log( datos)
  
    
      
  CamerasSummary.innerHTML = '';
        
        n = 0
        for(let dato of datos){
            n++;
            CamerasSummary.innerHTML += `
            <tr align="center">
                    <th scope="row">${ n }</th>
                    <td>${ dato.IdCam }</td>
                    <td>${ dato.HardwareName }</td>
                    <td>${ dato.CameraUse }</td>
                    <td>${ dato.IpCameraAddress }</td>
                    <td> <a href="${ dato.SnapshotUrl }">link Snapshot</a> </td>
                    <td><a href="${ dato.VideoUrl }">link Video</a></td>
                    <td>${ dato.Description }</td>
                    
					
                
            
            `;
			}
			
			})
		})
  })

  
// </script>