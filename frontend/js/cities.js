$("#create-cities-form").submit(function(e) {
    e.preventDefault()

    if($("#city_name").val() == "" )
        return;

    items={};
    items["city_name"] = $("#city_name").val();
    items["country_id"] = $("#country_id").val();
    items["zipcode"] = $("#zipcode").val();

    $.ajax( {
        url:"http://127.0.0.1:5000/api/cities/",
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
        url:"http://127.0.0.1:5000/api/cities/",
        
        method:"GET",
        crossDomain:true,
        dataType:"json",
        
        success:function(response){
            $.each(response,function(row){
                $("#tbody").append(
                    "<tr>"+
                        "<th scope='row' hidden>"+ response[row]['city_id']+"</th>"+
                        "<td class='ok'>"+ response[row]['city_name']+"</td>"+
                        "<td>"+ response[row]['name']+"</td>"+
                        "<td>"+ response[row]['zipcode']+"</td>"+
                        "<td><a id='edit-" + response[row]['city_id'] + "' class='btn btn-green' href='edit.html'><i class='fa fa-edit'></i></a> <a id='delete-" + response[row]['city_id'] + "' class='btn btn-red' href='#' onclick='deleteElement(this)'> <i class='fa fa-trash'></i> </a></td>"+
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
        url:"http://127.0.0.1:5000/api/cities/"+id,
        method:"GET",
        crossDomain:true,
        dataType:"json",
        success: function (result){
            $("#city_id").val(result["city_id"]);
            $("#city_name").val(result["city_name"]);
            $("#zipcode").val(result["zipcode"]);
            $("#country_id").val(result["country_id"])
        },
        error: function (error){
            var msg = error.responseText.split("<p>")[1].replace("</p>", "");
            noty(msg, "error")
        }
    }) 
}

function getAllCountries(){
    $.ajax( {
        url:"http://127.0.0.1:5000/api/countries/",
        method:"GET",
        crossDomain:true,
        dataType:"json",
        success: function (result){
            $.each(result,function(row){
                $("#country_id").append("<option value='"+ result[row]['country_id'] +"'>" + result[row]['name'] + "</option>")
            });
        },
        error: function (error){
            noty(error.responseText, 'error');
        }
    }) 
}

function deleteElement(e){
    var parent = $(e).parent().parent().children();
    var ville = $(parent[1]).html();
    var id = $(e).attr("id").split("-")[1];
    var deleteConfirm = confirm("Voulez-vous vraiment supprimer la ville: " + ville + " ?");
    if (deleteConfirm == true) {
        $.ajax( {
            url:"http://127.0.0.1:5000/api/cities/"+id,
            method:"DELETE",
            crossDomain:true,
            dataType:"json",
            success:function(response){
                noty(response, 'success');
                loadTable();
            },
            error:function(response){
                noty(response, 'success');
            }
        })
    }
}