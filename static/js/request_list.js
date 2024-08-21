function toggleText(element) {
    var moreText = element.previousElementSibling;
    
    if (moreText.style.display === 'none') {
        moreText.style.display = 'inline';
        element.textContent = 'See Less';
    } else {
        moreText.style.display = 'none';
        element.textContent = 'See More';
    }
}