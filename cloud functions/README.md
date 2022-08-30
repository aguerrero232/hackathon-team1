# Endpoints and Usage with examples

___

## **Team Member Endpoints**

* ### ***Create*** a new Team member

    Endpoint: https://us-central1-dell-hackathon-2022.cloudfunctions.net/create-tm

    method: **POST**

    **schema**: 

            {
                "id": string,
                "activated": bool,
                "cohort": string,
                "country": string,
                "date_joined": string,
                "date_last_active": string,
                "l4": string,
                "l5": string,
                "name": string,
                "new_course_enrolled": number,
                "new_course_started": number,
                "supervisor_id": string,
                "video_consumed": number,
                "work_region": string
            }


* ### ***Read*** team member data

    Endpoint: https://us-central1-dell-hackathon-2022.cloudfunctions.net/read-tm-data

    method: **GET**

    parameters:

        id: string

    **example usage:** https://us-central1-dell-hackathon-2022.cloudfunctions.net/read-tm-data?id={team member email}

* ### ***Read*** all team member data for specific supervisor

    Endpoint: https://us-central1-dell-hackathon-2022.cloudfunctions.net/get-all-tm

    method: **GET**

    parameters:

        id: string

    **example usage:** https://us-central1-dell-hackathon-2022.cloudfunctions.net/get-all-tm?id={manager email}

* ### ***Update*** a team member

    Endpoint: https://us-central1-dell-hackathon-2022.cloudfunctions.net/update-tm

    method: **POST**

    **schema**: 

            {
                "id": string,
                "activated": bool,
                "cohort": string,
                "country": string,
                "date_joined": string,
                "date_last_active": string,
                "l4": string,
                "l5": string,
                "name": string,
                "new_course_enrolled": number,
                "new_course_started": number,
                "supervisor_id": string,
                "video_consumed": number,
                "work_region": string
            }


___

## **Manager Endpoints**

* ### ***Create*** a new manager

    Endpoint: https://us-central1-dell-hackathon-2022.cloudfunctions.net/create-mngr

    method: **POST**

    **schema**: 

            {
                "id": string,
                "country": string,
                "l4": string,
                "l5": string,
                "name": string,
                "work_region": string
            }


* ### ***Read*** manager data

    Endpoint: https://us-central1-dell-hackathon-2022.cloudfunctions.net/read-mngr

    method: **GET**

    parameters:

        id: string

    **example usage:** https://us-central1-dell-hackathon-2022.cloudfunctions.net/read-mngr?id={manager email}

* ### ***Update*** a manager

    Endpoint: https://us-central1-dell-hackathon-2022.cloudfunctions.net/update-mngr

    method: **POST**

    **schema**: 

            {
                "id": string,
                "country": string,
                "l4": string,
                "l5": string,
                "name": string,
                "work_region": string
            }

___

## **Courses Endpoints**

* ### ***Create*** a new course

    Endpoint: https://us-central1-dell-hackathon-2022.cloudfunctions.net/create-course

    method: **POST**

    **schema**: 

            {
                "course_name": string,
                "course_description": string,
                "course_author": string,
                "course_source": string,
                "total_minutes": number
            }

* ### ***Read*** course data

    Endpoint: https://us-central1-dell-hackathon-2022.cloudfunctions.net/read-courses

    method: **GET**

    parameters:

        course_name: string

    **example usage:** https://us-central1-dell-hackathon-2022.cloudfunctions.net/read-courses?course_name={course name here}


* ### ***Update*** an existing course

    Endpoint: https://us-central1-dell-hackathon-2022.cloudfunctions.net/update-course

    method: **POST**

    **schema**: 

            {
                "course_name": string,
                "course_description": string,
                "course_author": string,
                "course_source": string,
                "total_minutes": number
            }