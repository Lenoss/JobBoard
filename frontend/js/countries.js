$("#create-country-form").submit(function(e) {
    e.preventDefault()

    items={};
    items["name"] = $("#name").val();

    $.ajax( {
        url:"http://127.0.0.1:5000/api/countries/",
        method:"POST",
        crossDomain:true,
        dataType:"json",
        data: items,
        success: function (result){
            console.log(result);
            noty(result, 'success');
        },
        error: function (error){
            console.log(error);
            var msg = error.responseText.split("<p>")[1].replace("</p>", "");
            noty(msg, "error")
        }
    }) 
})

function loadTable(){
    $("#tbody").empty();
    $.ajax( {
        url:"http://127.0.0.1:5000/api/countries/",
        
        method:"GET",
        crossDomain:true,
        dataType:"json",
        
        success:function(response){
            $.each(response,function(row){
                $("#tbody").append(
                    "<tr>"+
                        "<th scope='row' hidden>"+ response[row]['country_id']+"</th>"+
                        "<td>"+ response[row]['name']+"</td>"+
                        "<td><a id='edit-" + response[row]['country_id'] + "' class='btn btn-green' href='edit.html'><i class='fa fa-edit'></i></a> <a id='delete-" + response[row]['country_id'] + "' class='btn btn-red' href='#' onclick='deleteElement(this)'> <i class='fa fa-trash'></i> </a></td>"+
                    "</tr>"
                )
            });
        },
        error:function(error){
            var msg = error.responseText.split("<p>")[1].replace("</p>", "");
            noty(msg, "error")
        }
    });
}

function loadData(id){
    $.ajax( {
        url:"http://127.0.0.1:5000/api/countries/"+id,
        method:"GET",
        crossDomain:true,
        dataType:"json",
        success: function (result){
            $("#city_id").val(result["city_id"]);
            $("#name").val(result["name"]);
        },
        error: function (error){
            var msg = error.responseText.split("<p>")[1].replace("</p>", "");
            noty(msg, "error")
        }
    }) 
}

function deleteElement(e){
    var parent = $(e).parent().parent().children();
    var ville = $(parent[1]).html();
    var id = $(e).attr("id").split("-")[1];
    var deleteConfirm = confirm("Voulez-vous vraiment supprimer le pays: " + ville + " ?");
    if (deleteConfirm == true) {
        $.ajax( {
            url:"http://127.0.0.1:5000/api/countries/"+id,
            method:"DELETE",
            crossDomain:true,
            dataType:"json",
            success:function(response){
                noty(response, 'success');
                loadTable();
            },
            error:function(response){
                noty(response.responseText, 'error');
            }
        })
    }
}