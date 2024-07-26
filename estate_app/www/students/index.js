// document.addEventListener('DOMContentLoaded', () => {
    //     fetch('http://demo01.com:8003/api/method/estate_app.estate_app.api.student_api.get_students')
    //         .then(response => response.json())
    //         .then(students => {
    //             const studentList = document.getElementById('student-list');
    //             students.forEach(student => {
    //                 const studentCard = document.createElement('div');
    //                 studentCard.classList.add('student-card');
    //                 studentCard.innerHTML = `
    //                     <strong>Name:</strong> ${student.name1}<br>
    //                     <strong>Date of Birth:</strong> ${student.date_of_birth}<br>
    //                     <strong>Gender:</strong> ${student.gender}<br>
    //                     <strong>Email:</strong> ${student.email}<br>
    //                     <strong>Phone Number:</strong> ${student.phone_number}<br>
    //                     <strong>Department:</strong> ${student.department}<br>
    //                     <strong>Course:</strong> ${student.course}<br>
                        
    //                 `;
    //                 studentList.appendChild(studentCard);
    //             });
    //         })
    //         .catch(error => console.error('Error fetching students:', error));
    // });
    // Assuming this script is included in your HTML file within <script> tags
    
    // 
    
    // document.addEventListener('DOMContentLoaded', () => {
    //     fetch('http://demo01.com:8003/api/method/estate_app.estate_app.api.student_api.get_students')
    //         .then(response => response.json())
    //         .then(students => {
    //             const studentList = document.getElementById('student-list');
                
    //             students.message.forEach(student => {
    //                 const studentCard = document.createElement('div');
    //                 studentCard.classList.add('student-card');
    //                 studentCard.innerHTML = `
    //                     <p><strong>Register Number:</strong> ${student.register_number}</p>
    //                     <p><strong>Name:</strong> ${student.name1 || 'Not Available'}</p>
    //                     <p><strong>Date of Birth:</strong> ${student.date_of_birth || 'Not Available'}</p>
    //                     <p><strong>Gender:</strong> ${student.gender || 'Not Available'}</p>
    //                     <p><strong>Email:</strong> ${student.email || 'Not Available'}</p>
    //                     <p><strong>Phone Number:</strong> ${student.phone_number || 'Not Available'}</p>
    //                     <p><strong>Department:</strong> ${student.department || 'Not Available'}</p>
    //                     <p><strong>Course:</strong> ${student.course || 'Not Available'}</p>
    //                     <hr>
    //                 `;
    //                 studentList.appendChild(studentCard);
    //             });
    //         })
    //         .catch(error => console.error('Error fetching students:', error));
    // });
    
    document.addEventListener('DOMContentLoaded', () => {
        fetch('http://neha:8000/api/method/estate_app.api.student_api.get_students')
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                const studentList = document.getElementById('student-list');
                
                if (data && data.message) {
                    data.message.forEach(student => {
                        const studentCard = document.createElement('div');
                        studentCard.classList.add('student-card');
                        studentCard.innerHTML = `
                            <p><strong>Reg No:</strong> ${student.reg_no}</p>
                            <p><strong>Name:</strong> ${student.name1 || 'Not Available'}</p>
                            <p><strong>DOB:</strong> ${student.dob || 'Not Available'}</p>
                            <p><strong>Gender:</strong> ${student.gender || 'Not Available'}</p>
                            <p><strong>Email:</strong> ${student.email || 'Not Available'}</p>
                            <p><strong>Phone :</strong> ${student.phone || 'Not Available'}</p>
                            <p><strong>Department:</strong> ${student.department || 'Not Available'}</p>
                            <p><strong>Course:</strong> ${student.course || 'Not Available'}</p>
                            <hr>
                        `;
                        studentList.appendChild(studentCard);
                    });
                } else {
                    studentList.innerHTML = '<p>No students found.</p>';
                }
            })
            .catch(error => {
                console.error('Error fetching students:', error);
                document.getElementById('student-list').innerHTML = '<p>Error fetching students.</p>';
            });
    });
    