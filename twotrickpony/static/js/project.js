

/* Project specific Javascript goes here. */
var rotate = document.getElementById( 'logo' );
if (rotate) {
    rotate.addEventListener( 'mouseover', function () {
    
        this.className = 'over';
    
    }, false );
    
    rotate.addEventListener( 'mouseout', function () {
    
        var rotate = this;
    
        rotate.className = 'out';
        window.setTimeout( function () { rotate.className = '' }, 150 );
    
    }, false );
    window.setTimeout(function() {rotate.className = 'over';}, 150);
    window.setTimeout(function() {rotate.className = 'out';}, 300);
}



// var collapseElementList = [].slice.call(document.querySelectorAll('.collapse'))
// var collapseList = collapseElementList.map(function (collapseEl) {
//   return new bootstrap.Collapse(collapseEl)
// })