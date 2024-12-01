// Defining a data model.
class Resume {
  basics Basics?
  skills Skills?
  work Work?
  education Education?
  activities Activites?
}

class Basics {
  name string? @description(#"
    Name of the person.
  "#)
  label string? @description(#"
    If mentioned, what is the job title of the person?
  "#)
  email string? @description(#"
    Professional email
  "#)
  image string? @description(#"
    If mentioned, what is the url of the person's image?"#)

  phone string? @description(#"
    Phone number of this person.
  "#)
  url string? @description(#"
    URL of personal website.
  "#)
  summary string? @description(#"
    Write the about me / summary section of the resume in first person.
  "#)
  location Location

  relExp string? @description(#"
    What is the total years of relevant experience of the person?"#)

  totalExp string? @description(#"
    What is the total years of experience of the person?"#)
  
  objective string? @description(#"
    Write in first person what this person wants to do next in career."#)
  
  profiles Profile[] | null @description(#"
    List of social media profiles of the person."#)
}

class Location {
  address string? @description(#"
   Address of the person.
  "#)
  postalCode string? @description(#"
  "#)
  city string? @description(#"
    city in which the person resides.
  "#)
  countryCode string? @description(#"
  "#)
  region string? @description(#"
  "#)
}

class Profile{
  network string? @description(#"
    Name of the social network"#)
  username string? @description(#"
    username of the person on this network?"#)
  url string? @description(#"
    url of the person on this network?"#)
}


class Skills {
  languages SkillDetails[] | null @description(#"
    What programming languages does this person know?
  "#)
  frameworks SkillDetails[] | null @description(#"
    What frameworks has this person know as per CV?"#)
  technologies SkillDetails[] | null @description(#"
    What technologies has this person mentioned in the CV?
  "#)
  libraries SkillDetails[] | null @description(#"
    What libraries has this person mentioned in the CV?
  "#) 
}

class SkillDetails {
  name string? @description(#"
    name of the skill?
  "#)
  level int? @description(#"
   level of the skill?
  "#)
}

class Education {
  universities University[] | null @description(#"
    List of universities the person has attended. Usually under the education header.
  "#)
}

class University {
  id string? @description(#"
    Increamental"#)

  name string? @description(#"
    name of the university
  "#)

  url string? @description(#"
    URL of the university"#)

  studyType string? @description(#"
    degree obtained by the person from this university?
  "#)

  area string? @description(#"
   major of the person in this degree?
  "#)

  startDate string?
  
  endDate string? 

  score string? @description(#"
    Score or GPA obtained of the person in this degree?
  "#)
  courses string[] | null @description(#"
    List of courses taken by the person in this degree.
  "#)
}

class Work {
  companies Company[] | null @description(#"
    List of companies or organizations the person has worked at. Usually under the experience header.
  "#)
}

class Company {
  id string? @description(#"
    Increamental"#)

  name string?
  position string? @description(#"
    job title or position of the person at this company?
  "#)
  url string? @description(#"
    URL of the company"#)
  startDate string?
  endDate string? 
  highlights string[] | null @description(#"
    What work did the person do at this company?
    What responsibilites were handeled by the person at this company?
  "#)
  summary string? 
}
class Activites {
  involvements string? @description(#"
    Describe the person's involvement in the community or any other activities.
  "#)
  achievements string? @description(#"
    Describe the person's certifications mentioned in the resume."
  "#)
  volunteer Volunteer[] | null @description(#"
    List of volunteer work done by the person.
  "#)

  awards Award[] | null @description(#"
    List of awards/certificates the person has received. Usually under the Awards Header.
  "#)

}

class Volunteer {
  id string? @description(#"
    Increamental"#)
  organization string? @description(#"
    name of the project?
  "#)
  position string? @description(#"
    position of the person in this organization?
  "#)
  url string? @description(#"
    URL of the organization"#)
  startDate string?
  endDate string?
  summary string? @description(#"
    What was the summary of the work done at this organization?
  "#)
  highlights string[] | null @description(#"
    What work did the person do at this organization?
    What responsibilites were handeled by the person at this organization?
  "#)
  isVolunteeringNow bool?
}

class Award {
  id string?
  title string? @description(#"
    title of the award?
  "#)
  date string?
  awarder string? @description(#"
    Who gave the award?
  "#)
  summary string?
}


// Create a function to extract the resume from a string.
function ExtractResume(resume: string, jobdescription: string) -> Resume {
  // Specify a client as provider/model-name
  // you can use custom LLM params with a custom client name from clients.baml like "client CustomHaiku"
  client Llama3_2 // Set OPENAI_API_KEY to use this client.
  prompt #" 
    {{_.role('system')}}

    <|start_header_id|>system<|end_header_id|>
    Your task is to rewrite the given CV to fit the job description. Follow these guidelines:
     Be truthful and objective to the experience listed in the CV.
     Rearrange projects and skills according to the requirement of the job
     Rewrite Job descriptions that match the job description but is also truthful
     Fix spelling and grammar errors
     Remove irrelevant information.
    <|eot_id|>

    {{_.role('user')}}
    <|start_header_id|>user<|end_header_id|>
    Given a resume
    {{ resume }}
    
    and a job description 
    {{ jobdescription }},
    
    Extract from the updated CV. If no value is available for a field, provide an null value. <|eot_id|>
    
    {{ ctx.output_format }}
  "#
}

// Test the function with a sample resume. Open the VSCode playground to run this.
test vaibhav_resume {
  functions [ExtractResume]
  args {
    resume #"
      Vaibhav Gupta
      vbv@boundaryml.com

      Experience:
      - Founder at BoundaryML
      - CV Engineer at Google
      - CV Engineer at Microsoft

      Skills:
      - Rust
      - C++
    "#,
    jobdescription #"
      Software Engineer
    "#
  }
}
