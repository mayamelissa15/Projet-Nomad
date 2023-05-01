const stars = document.querySelectorAll('.star');
// on va faire une boucle through the stars

stars.forEach((star ,index1) => 
{
  star.addEventListener("click" , ()=> {
    stars.forEach((star ,index2) => {
      // on va ajouter la classe active a chaque fois qu'on clique sur une etoile avec un index inferieur et la remove de celui de l'index superieur 
      index1 >= index2 ? star.classList.add("active") : star.classList.remove("active")
    });
  });
});