function onUpdateGoods(gid,page) {
    location.href='/goods/update_goods?gid=' + gid + '&p='+ page;
}

function onUpdateStatus(gid,page) {
    location.href='/goods/update_status?gid=' + gid + '&p='+ page;
}

function onSendVerifyMail() {

    $.ajax({
        type: "POST",
        url: "/login/sendVerifyMail"
    }).done(function( o ) {
       //$('#myModal').modal('hide');
    });

}