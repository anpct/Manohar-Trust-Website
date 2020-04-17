$(document).ready(
    function add_mail(){
        $('a[id^=add]').on("click", function (e) {
            var mailformat = /^w+([.-]?w+)*@w+([.-]?w+)*(.w{2,3})+$/;
            var mail = document.getElementById('emaila').value;
            var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
            if(mail == "")
                    {
                        alert("Enter a valid email");
                        return;
                    }
            if( !(emailReg.test( mail )))
            {
                alert("Enter a valid email");
return;
            }
            $.ajax({
                url : "add_mail/", 
                type : "POST",
                data: {
                    mail : mail
                },
                success : function(data) {
                    alert("THANK YOU FOR SUBSCRIBING");
                },
                error: function (data) {
                  alert("SOMETHING WENT WRONG");
                } 
            });
       
    })
    }
    );