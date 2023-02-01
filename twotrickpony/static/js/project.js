

/* Project specific Javascript goes here. */
var rotate = document.getElementById( 'logo' );

rotate.addEventListener( 'mouseover', function () {

    this.className = 'over';

}, false );

rotate.addEventListener( 'mouseout', function () {

    var rotate = this;

    rotate.className = 'out';
    window.setTimeout( function () { rotate.className = '' }, 150 );

}, false );


// var collapseElementList = [].slice.call(document.querySelectorAll('.collapse'))
// var collapseList = collapseElementList.map(function (collapseEl) {
//   return new bootstrap.Collapse(collapseEl)
// })