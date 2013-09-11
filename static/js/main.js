/*
 * Change site theme to new value, reload page...
 *
 */
function theme(name){
    $.cookie('theme',name, { expires: 7, path: '/' });
    //reload...
    location.reload();
}
