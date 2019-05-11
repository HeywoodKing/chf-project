KindEditor.ready(function(K){
    var options = {
        filterMode : true,
        allowImageUpload : false,
        allowFlashUpload : false,
        allowMediaUpload : false,
        allowFileManager : false,
        items : ['fontname', 'fontsize', '|', 'forecolor', 'hilitecolor', 'bold', 'italic', 'underline',
        'removeformat', '|', 'justifyleft', 'justifycenter', 'justifyright', 'insertorderedlist',
        'insertunorderedlist', '|', 'emoticons', 'image', 'flash', 'media','|', 'link','unlink','fullscreen'],
        width : '680px',
        height: '600px'
    };

    var editor = new Array();
    editor[0] = K.create('textarea[name=content]', {
        width:'680px',
        height:'600px',
        resizeType:1,
        allowPreviewEmoticons: false,
        allowImageRemote: false,
        uploadJson: '/admin/upload/kindeditor',
    });
    /*editor[1] = K.create('textarea[name="job_require"]', {
        width:'680px',
        height:'600px',
        resizeType:1,
        allowPreviewEmoticons: false,
        allowImageRemote: false,
        uploadJson: '/admin/upload/kindeditor',
    });
    editor[2] = K.create('textarea[name=skill_require]', {
        width:'680px',
        height:'600px',
        resizeType:1,
        allowPreviewEmoticons: false,
        allowImageRemote: false,
        uploadJson: '/admin/upload/kindeditor',
    });*/
});