/**
 * Created by wxy on 15/12/14.
 */

function regist(){
    $("#regist").click(
        function(){
            $.get("/regist_form",function(tmp1){
               $("#demo").html(tmp1);
            });
        }
    );
    $("#signin").click(
        function(){
            $.get("/login_form",function(tmp2){
                $("#demo").html(tmp2);
            });
        }
    );
}

$(document).ready(

    function(){
        $.get("/login_form",function(data)
        {
            $("#demo").html(data);
            regist();
        });
    }
);

