document.getElementsById("inscription").addEventlistener('submit', function(e)
{   e.preventdefault(); // pour eviter le comportement par defaut de la page qui est son rechargement automatique 
    alert("Formulaire envoyé !");
}// cet evenement sera declenché automatiquement quand le formulaire sera envoyé 



)