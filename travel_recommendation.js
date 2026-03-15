function searchPlace(){

let input=document.getElementById("searchInput").value.toLowerCase();

let results=document.getElementById("results");

if(input.includes("beach")){
results.innerHTML="<h2>Beaches</h2><p>Maldives Beach</p><p>Goa Beach</p>";
}

else if(input.includes("temple")){
results.innerHTML="<h2>Temples</h2><p>Golden Temple</p><p>Meenakshi Temple</p>";
}

else if(input.includes("country")){
results.innerHTML="<h2>Countries</h2><p>India</p><p>Japan</p>";
}

else{
results.innerHTML="<p>No results found</p>";
}

}

function clearResults(){
document.getElementById("results").innerHTML="";
}