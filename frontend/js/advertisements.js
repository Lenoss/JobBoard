$("#create-advertisements-form").submit(function(e) {
    e.preventDefault()

    // if($("#title").val() == "" )
    //     return;

    items={};
    items["title"] = $("#title").val();

    $.ajax( {
        url:"http://127.0.0.1:5000/api/advertisements/",
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
        url:"http://127.0.0.1:5000/api/advertisements/",
        
        method:"GET",
        crossDomain:true,
        dataType:"json",
        success:function(response){
            $.each(response,function(row){
                $("#tbody").append(
                    "<tr>"+
                        "<th scope='row' hidden>"+ response[row]['advertisement_id']+"</th>"+
                        "<td>"+ response[row]['title']+"</td>"+
                        "<td>"+ response[row]['description']+"</td>"+
                        "<td>"+ response[row]['company_name']+"</td>"+
                        "<td>"+ response[row]['city_name']+"</td>"+
                        "<td>"+ response[row]['sector']+"</td>"+
                        "<td>"+ response[row]['contract']+"</td>"+
                        "<td>"+ response[row]['wages']+"</td>"+
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
        url:"http://127.0.0.1:5000/api/advertisements/"+id,
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
    var advertisement_id = $(parent[1]).html();
    var id = $(e).attr("id").split("-")[1];
    var deleteConfirm = confirm("Do you really want to delete the advertisement " + advertisement_id + " ?");
    if (deleteConfirm == true) {
        $.ajax( {
            url:"http://127.0.0.1:5000/api/advertisements/" + advertisement_id,
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



function loadSelectCountries(){
    $.ajax( {
        url:"http://127.0.0.1:5000/api/countries/",
        method:"GET",
        crossDomain:true,
        dataType:"json",
        success: function (result){
            $("#country_id").append("<option value='0'>-- You have to select a city --</option>");
            $.each(result,function(row){
                $("#country_id").append("<option value='"+ result[row]['country_id'] +"'>" + result[row]['name'] + "</option>")
            });
        },
        error: function (error){
            noty(error.responseText, 'error');
        }
    }) 
}

function loadSelectCities(){
    $.ajax( {
        url:"http://127.0.0.1:5000/api/cities/",
        method:"GET",
        crossDomain:true,
        dataType:"json",
        success: function (result){
            $("#city_id").append("<option value='0'>-- Select a city --</option>");
            $.each(result,function(row){
                $("#city_id").append("<option value='"+ result[row]['city_id'] +"'>" + result[row]['city_name'] + "</option>")
            });
        },
        error: function (error){
            noty(error.responseText, 'error');
        }
    }) 
}

function loadSelectContractTypes(){
    $.ajax( {
        url:"http://127.0.0.1:5000/api/contract_types/",
        method:"GET",
        crossDomain:true,
        dataType:"json",
        success: function (result){
            $("#contract_type").append("<option value='0'>-- Select a contract type --</option>");
            $.each(result,function(row){
                $("#contract_type").append("<option value='"+ result[row]['type_id'] +"'>" + result[row]['contract'] + "</option>")
            });
        },
        error: function (error){
            noty(error.responseText, 'error');
        }
    }) 
}