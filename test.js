function leadTimeModal(n){
  var i={}, r, t, u;
  $(".content-leadtime-form").serializeArray().map(function(n){i[n.name]=n.value}),r=JSON.stringify(i),t=JSON.parse(r),t.partid&&t.partid!=0||(u=utag_data.part_id,t.partid=u),n.preventDefault?n.preventDefault():n.returnValue=!1,$.ajax({type:"POST",url:leadTimeurl,data:t,timeout:digireelTimeout,success:function(n){$("#leadTimeHolder").html(n),$("#leadTimePopup").dialog({modal:!0,width:400,draggable:!1,closeOnEscape:!0,close:function(){$(this).dialog("destroy").remove()}

var leadTimeurl = "https://www.digikey.com/product-detail/leadtime/en/"
//type:"POST",url:leadTimeurl,data
