var data = document.querySelector('.audio').attributes['data-audio'].value;
if (data) {
    var url = 'https://audio.vocab.com/1.0/us/' + data + '.mp3';
    var filename = document.title.split('-')[0].trim() + '.mp3';
    download(filename, url);
}
function download(filename, text) {
    var pom = document.createElement('a');
    pom.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    pom.setAttribute('download', filename);

    if (document.createEvent) {
        var event = document.createEvent('MouseEvents');
        event.initEvent('click', true, true);
        pom.dispatchEvent(event);
    }
    else {
        pom.click();
    }
}
