$("#create-contract-form").submit(function(e) {
    e.preventDefault()

    if($("#contract").val() == "" )
        return;

    items={};
    items["contract"] = $("#contract").val();

    $.ajax( {
        url:"http://127.0.0.1:5000/api/contract_types/",
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
        url:"http://127.0.0.1:5000/api/contract_types/",
        
        method:"GET",
        crossDomain:true,
        dataType:"json",
        
        success:function(response){
            $.each(response,function(row){
                $("#tbody").append(
                    "<tr>"+
                        "<th scope='row' hidden>"+ response[row]['type_id']+"</th>"+
                        "<td class='ok'>"+ response[row]['contract']+"</td>"+
                        "<td><a id='edit-" + response[row]['type_id'] + "' class='btn btn-green' href='edit.html'><i class='fa fa-edit'></i></a> <a id='delete-" + response[row]['type_id'] + "' class='btn btn-red' href='#' onclick='deleteElement(this)'> <i class='fa fa-trash'></i> </a></td>"+
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
        url:"http://127.0.0.1:5000/api/contract_types/"+id,
        method:"GET",
        crossDomain:true,
        dataType:"json",
        success: function (result){
            $("#type_id").val(result["type_id"]);
            $("#contract").val(result["contract"]);
        },
        error: function (error){
            var msg = error.responseText.split("<p>")[1].replace("</p>", "");
            noty(msg, "error")
        }
    }) 
}

function getAllContracts(){
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
    var contract = $(parent[1]).html();
    var id = $(e).attr("id").split("-")[1];
    var deleteConfirm = confirm("Do you really want to delete the contract type : " + contract + " ?");
    if (deleteConfirm == true) {
        $.ajax( {
            url:"http://127.0.0.1:5000/api/contract_types/"+id,
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