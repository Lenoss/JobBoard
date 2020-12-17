$("#create-roles-form").submit(function(e) {
    e.preventDefault()

    if($("#title").val() == "" )
        return;

    items={};
    items["title"] = $("#title").val();

    $.ajax( {
        url:"http://127.0.0.1:5000/api/roles/",
        method:"POST",
        crossDomain:true,
        dataType:"json",
        data: items,
        success: function (result){
            noty(result, 'success');
        },
        error: function (error){
            var msg = error.responseText.split("<p>")[1].replace("</p>", "");
            noty(msg, "error")
        }
    }) 
})

function loadTable(){
    $("#tbody").empty();
    $.ajax( {
        url:"http://127.0.0.1:5000/api/roles/",
        
        method:"GET",
        crossDomain:true,
        dataType:"json",
        
        success:function(response){
            $.each(response,function(row){
                $("#tbody").append(
                    "<tr>"+
                        "<th scope='row' hidden>"+ response[row]['role_id']+"</th>"+
                        "<td>"+ response[row]['title']+"</td>"+
                        "<td><a id='edit-" + response[row]['role_id'] + "' class='btn btn-green' href='edit.html'><i class='fa fa-edit'></i></a> <a id='delete-" + response[row]['role_id'] + "' class='btn btn-red' href='#' onclick='deleteElement(this)'> <i class='fa fa-trash'></i> </a></td>"+
                    "</tr>"
                )
            });
        },
        error:function(response){
            console.log("Error");
            console.log(response);
        }
    });
}


function loadData(id){
    $.ajax( {
        url:"http://127.0.0.1:5000/api/roles/"+id,
        method:"GET",
        crossDomain:true,
        dataType:"json",
        success: function (result){
            $("#role_id").val(result["role_id"]);
            $("#title").val(result["title"]);
        },
        error: function (error){
            var msg = error.responseText.split("<p>")[1].replace("</p>", "");
            noty(msg, "error")
        }
    }) 
}

function deleteElement(e){
    var parent = $(e).parent().parent().children();
    var role = $(parent[1]).html();
    var id = $(e).attr("id").split("-")[1];
    var deleteConfirm = confirm("Do you really want to delete the role " + role + " ?");
    if (deleteConfirm == true) {
        $.ajax( {
            url:"http://127.0.0.1:5000/api/roles/"+id,
            method:"DELETE",
            crossDomain:true,
            dataType:"json",
            success:function(response){
                noty(response, 'success');
                loadTable();
            },
            error:function(response){
                noty(response, 'error');
            }
        })
    }
}