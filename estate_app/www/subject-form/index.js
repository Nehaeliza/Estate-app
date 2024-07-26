$('#subject-form').submit(e=>{
    e.preventDefault();
    // upload method
    makecall();
    // console.log(e.target)
})
// upload method
let makecall = async()=>{
    let formdata = $('#subject-form').serializeArray().reduce(
        (obj, item)=>(obj[item.name]=item.value, obj), {}
    );
    let imagedata = $('#image')[0].files[0];
    // initialize form
    let imagefile = new FormData()
    if(imagedata){
        imagefile.append('file',imagedata);
    }
    // end initialize

    // post to API
    if(formdata){
        let res = await $.ajax({
            url: 'http://localhost:8000/api/resource/Subject',
            type: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Frappe-CSRF-Token': frappe.csrf_token
            },
            data: JSON.stringify(formdata),
            success: function(data){
                return data
            },
            error: function(data){
                return data
            }
        })
        console.log(res);

        //upload image
        if(res.data && imagedata){
            let imgres = await fetch('http://localhost:8000/api/method/upload_file',{
                headers:{ 
                    'X-Frappe-CSRF-Token': frappe.csrf_token

                },
                method: 'POST',
                body: imagefile
                
            })
            .then(res=>res.json())
            .then(data=>{
                console.log(data);
                if(data.message){
                    $.ajax({
                        url: 'http://localhost:8000/api/resource/Subject/${res.data.name}',
                        type: 'PUT',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-Frappe-CSRF-Token': frappe.csrf_token
                        },
                        data: JSON.stringify({image:data.message.file_url}),
                        success: function(data){
                            return data
                        },
                        error: function(data){
                            return data
                        }
                    })

                }

            })
        }

    }
}


// $('#subject-form').submit(e => {
//     e.preventDefault();
//     makecall();
// });

// let makecall = async () => {
//     let formdata = $('#subject-form').serializeArray().reduce(
//         (obj, item) => (obj[item.name] = item.value, obj), {}
//     );

//     console.log("Form data:", formdata);  // Debugging line

//     let imagedata = $('#image')[0].files[0];
//     let imagefile = new FormData();
//     if (imagedata) {
//         imagefile.append('file', imagedata);
//         console.log("Image data:", imagedata);  // Debugging line
//     }

//     // Post form data to the API
//     if (formdata) {
//         try {
//             let res = await $.ajax({
//                 url: 'http://localhost:8000/api/resource/Subject',
//                 type: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                     'X-Frappe-CSRF-Token': frappe.csrf_token
//                 },
//                 data: JSON.stringify(formdata)
//             });

//             console.log('Form submission response:', res);

//             // Upload image if form submission is successful
//             if (res.data && imagedata) {
//                 let imgres = await fetch('http://localhost:8000/api/method/upload_file', {
//                     headers: {
//                         'X-Frappe-CSRF-Token': frappe.csrf_token
//                     },
//                     method: 'POST',
//                     body: imagefile
//                 }).then(res => res.json());

//                 console.log('Image upload response:', imgres);

//                 if (imgres.message) {
//                     let updateRes = await $.ajax({
//                         url: `http://localhost:8000/api/resource/Subject/${res.data.name}`,
//                         type: 'PUT',
//                         headers: {
//                             'Content-Type': 'application/json',
//                             'X-Frappe-CSRF-Token': frappe.csrf_token
//                         },
//                         data: JSON.stringify({ image: imgres.message.file_url })
//                     });

//                     console.log('Update response:', updateRes);
//                 }
//             }
//         } catch (error) {
//             console.error('Error:', error);
//         }
//     }
// };
