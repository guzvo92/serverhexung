/* Atacando objetos

var player = {
  name : "digibyte",
  lvl : 100,
  voc : "sorcerer",
}

//accesores a propiedades de obj
forma1 = player.lvl
forma2 = player['lvl']

console.log (player) //objeto
console.log ("[1] " + forma1)  //100
console.log ("[2] " + forma2)  //100

for (var x in player){
  if (player.hasOwnProperty(x)){
    sun = ${player}.${x}
    console.log ("[3] " + sun )
  }
}

*/
// === igualdad estricta ( operadores del mismo tipo y contenidos coinciden)
//console.log(`Hola ${m} ${m} `)
//array = ["g","m","h"];

count = 0
string = "";

fn = (input) => {
  inputsplit = input.split("")
  for (let i of inputsplit){
    count ++;
    for (let m=1; m<=count; m++){
      if (m==1){string += i.toUpperCase()}
      else {string += i.toLowerCase()}
    }; //endfor
    string += "-";
  }//end mainfor
  num = (string.length) - 1;
  laststring = string.substring(0, num);
  console.log(laststring)
  return laststring
}

fn("xdshs");


function x (){
  console.log("Hello")
}
x();
