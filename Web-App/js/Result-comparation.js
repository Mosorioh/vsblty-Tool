//<!-- Get all paises -->
//<script>
    //fetch('http://181.199.66.129:5010/pais')
    fetch('http://181.199.66.129:5080/selectcomparation/Multiple')
    .then(ListTest=>ListTest.json())
    .then(ListTest=>{
      console.log("Test-----------")
        console.log(ListTest)
        
        var resultado = document.getElementById('Test1');
        var n = 0;
        Test1.innerHTML = '';
        Test1.innerHTML = '<option selected="Test1">Test Numero</option>';
        
        for(let dato of ListTest){
            n++;
            resultado.innerHTML += `
            <option value="${dato.Id}"> (${dato.Id}) - ${dato.GUID} - ${dato.CameraMode} Camera - ${dato.Hostname} - ${dato.Descripcion}</option>
            
            `;
           
        }
       
    })
    
//</script>


//console.log ("Conexion js Link")
//<!----- Script 1------>
//<!-- Get all paises -->
//<script>
    //fetch('http://192.168.100.233:5080/selectcomparation/Simple')
    fetch('http://181.199.66.129:5080/selectcomparation/Simple')
    .then(ListTest=>ListTest.json())
    .then(ListTest=>{
      console.log("---- Test comparation--")
        console.log(ListTest)
        
        var resultado = document.getElementById('Test2');
        var n = 0;
        Test2.innerHTML = '';
        Test2.innerHTML = '<option selected="Test2">Test Number</option>';
        
        for(let dato of ListTest){
            n++;
            resultado.innerHTML += `
            <option value="${dato.Id}"> (${dato.Id}) - ${dato.GUID} - ${dato.CameraMode} Camera - ${dato.Hostname} - ${dato.Descripcion}</option>
            
            `;
           
        }
        var resultado = document.getElementById('Test3');
        var n = 0;
        Test3.innerHTML = '';
        Test3.innerHTML = '<option selected="Test3">Test Number</option>';
        
        for(let dato of ListTest){
            n++;
            resultado.innerHTML += `
            <option value="${dato.Id}"> (${dato.Id}) - ${dato.GUID} - ${dato.CameraMode} Camera - ${dato.Hostname} - ${dato.Descripcion}</option>
            
            `;
           
        }
       
       
    })
    
//</script>


//

//


//<!----- Script 3------>
//<!-- get provincia Segun opcion seleccionada en el drowndoon-->
//<script>	  
$(document).ready(function(){
    $("#Test1").on("change",function(){						
      var TestMultiplenumero =$(this).val()//obtenemos el valor seleccionado en una variable	
      //console.log("Test Seleccionado: " + Testnumero) 
  
     fetch('http://181.199.66.129:5080/ResumenCiclo/'+TestMultiplenumero+'/1')
  
      .then(datos=>datos.json())
      .then(datos=>{
    console.log("****Resultado resumen ciclo multipple")   
    console.log( datos)
    
      
        
    ResumenCiclo1.innerHTML = '';
          
          n = 0
          for(let dato of datos){
              n++;
              ResumenCiclo1.innerHTML += `
              <tr>
                      <th scope="row">${ n }</th>
                      
                      
                      <td>${ dato.TotalIdentificacion }</td>
                      <td>${ dato.TotalFrameReceived }</td>
                      <td>${ dato.TotalBeforeProcessing }</td>
                      <td>${ dato.TotalFrameReceived - dato.TotalBeforeProcessing }</td>
                      <td>${ dato.TotalFaceAPIResults }</td>
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
    $("#Test1").on("change",function(){						
      var TestMultiplenumero =$(this).val()//obtenemos el valor seleccionado en una variable	
      console.log("Test Multiple Seleccionado: " + TestMultiplenumero) 


  
     fetch('http://181.199.66.129:5080/Testnumero/'+TestMultiplenumero+'/1')
  
      .then(datos=>datos.json())
      .then(datos=>{
    console.log("Resultado Multiplw-------------")   
    console.log( datos)
    
      
        
    contenido1.innerHTML = '';
          
          n = 0
          for(let dato of datos){
              n++;
              contenido1.innerHTML += `
              <tr>
                      
              <th scope="row">${ n }</th>
              
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
    $("#Test2").on("change",function(){						
      var TestSimple1 =$(this).val()//obtenemos el valor seleccionado en una variable	
      console.log("Test 1 Seleccionado: " + TestSimple1) 

  
     fetch('http://181.199.66.129:5080/ResumenCiclo/'+TestSimple1+'/1')
  
      .then(datos=>datos.json())
      .then(datos=>{
    console.log("****Resultado resumen ciclo multipple")   
    console.log( datos)
    
      
        
    ResumenCiclo2.innerHTML = '';
          
          n = 0
          for(let dato of datos){
              n++;
              ResumenCiclo2.innerHTML += `
              <tr>
                      <th scope="row">${ n }</th>
                      
                      
                      <td>${ dato.TotalIdentificacion }</td>
                      <td>${ dato.TotalFrameReceived }</td>
                      <td>${ dato.TotalBeforeProcessing }</td>
                      <td>${ dato.TotalFrameReceived - dato.TotalBeforeProcessing }</td>
                      <td>${ dato.TotalFaceAPIResults }</td>
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
    $("#Test2").on("change",function(){						
      var TestSimple1 =$(this).val()//obtenemos el valor seleccionado en una variable	
      console.log("Test 1 Seleccionado: " + TestSimple1) 


  
     fetch('http://181.199.66.129:5080/Testnumero/'+TestSimple1+'/1')
  
      .then(datos=>datos.json())
      .then(datos=>{
    console.log("Resultado Multiplw-------------")   
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
    $("#Test3").on("change",function(){						
      var TestSimple2 =$(this).val()//obtenemos el valor seleccionado en una variable	
      console.log("Test Simple 2: " + TestSimple2) 
  
     fetch('http://181.199.66.129:5080/ResumenCiclo/'+TestSimple2+'/1')
  
      .then(datos=>datos.json())
      .then(datos=>{
    console.log("****Resultado resumen ciclo multipple")   
    console.log( datos)
    
      
        
    ResumenCiclo3.innerHTML = '';
          
          n = 0
          for(let dato of datos){
              n++;
              ResumenCiclo3.innerHTML += `
              <tr>
                      <th scope="row">${ n }</th>
                      
                      
                      <td>${ dato.TotalIdentificacion }</td>
                      <td>${ dato.TotalFrameReceived }</td>
                      <td>${ dato.TotalBeforeProcessing }</td>
                      <td>${ dato.TotalFrameReceived - dato.TotalBeforeProcessing }</td>
                      <td>${ dato.TotalFaceAPIResults }</td>
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
    $("#Test3").on("change",function(){						
      var TestSimple2 =$(this).val()//obtenemos el valor seleccionado en una variable	
      console.log("--Test simple 2: " + TestSimple2) 


  
     fetch('http://181.199.66.129:5080/Testnumero/'+TestSimple2+'/1')
  
      .then(datos=>datos.json())
      .then(datos=>{
    console.log("Resultado simple  2-------------")   
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