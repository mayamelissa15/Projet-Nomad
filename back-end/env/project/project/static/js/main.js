    
        window.addEventListener('scroll' , reveal);
        function reveal(){
        var reveals = document.querySelectorAll('.reveal')
        for ( var i=0 ; i< reveals.length ;i++)// pour parcourir tous nos elements dont la classe est reveal
        {
            var windowheight = window.innerHeight;
            var revealtop = reveals[i].getBoundingClientRect().top ; 
            var revealpoint=150;

            if (revealtop < windowheight - revealpoint)
            {
                reveals[i].classList.add('active');
            }
            else
            {
            reveals[i].classList.remove('active');
            }
        }

        }
        
        window.addEventListener('DOMContentLoaded' , () =>
        {
        const menuBtn= document.querySelector('#menu-btn')
        const dropdown= document.querySelector('#dropdown')
        menuBtn.addEventListener('click', ()=> {
            if(dropdown.classList.contains('hidden'))
            {
              dropdown.classList.remove('hidden') ;
              dropdown.classList.add('flex');
            }
            else{
              dropdown.classList.remove('flex')
              dropdown.classList.add('hidden')
            }
        })
        })

