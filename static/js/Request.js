class Request{
    static post = async (url, data) => {
        let result = $.ajax({
            async: false,
            type: "POST",
            url: url,
            data: JSON.stringify(data),
            contentType: "application/json",
            success : (response) => {
                return response;
            }           
        });
        return result;
    }
}