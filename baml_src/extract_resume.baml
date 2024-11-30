// Defining a data model.
class Resume {
  basic_details BasicDetails
  skills_and_expertise SkillsAndExpertise
  education Education
  experience Experience
  projects PersonalProjects
  awards Awards
}

class BasicDetails {
  contacts Contacts
  links Links
  about_me string @description(#"
    Write the about me section of the resume in first person.
  "#)
}

class Contacts {
  name string @description(#"
    What is the name of the person?
  "#)
  title string @description(#"
    If mentioned, what is the job title of the person?
  "#)
  email string @description(#"
    If mentioned, what is the professional email of the person?
  "#)
  phone string @description(#"
    If mentioned, what is the phone number of the person?
  "#)
  websiteURL string @description(#"
    If mentioned, what is the url of the person's website?
  "#)
}

class Links {
  linkedin string
  github string
  others string[] 
}

class SkillsAndExpertise {
  programming_languages_known string[]
  frameworks_known string[]
  technologies_used string[]
  languagees_known string[] @description(#"
    What languages does this person speak?
  "#) 
}

class Education {
  universities University[] @description(#"
    List of universities the person has attended. Usually under the education header.
  "#)
}

class University {
  name string @description(#"
    What is the name of the university?
  "#)
  degree string @description(#"
    What is the degree obtained by the person from this university?"#)
  major string @description(#"
    What is the major of the person in this degree?
  "#)
  score string @description(#"
    What is the score or GPA obtained by the person in this degree?
  "#)
  startdate string
  @description(#"
    When did the person start studying at this university?
  "#)
  enddate string @description(#"
    When did the person finish studying at this university?"#)
}

class Experience {
  companies Company[] @description(#"
    List of companies or organizations the person has worked at. Usually under the experience header.
  "#)
}

class Company {
  name string
  position string @description(#"
    What was the job title or position of the person at this company?
  "#)
  startdate string @description(#"
    When did the person start working at this company?
  "#)
  enddate string @description(#"
    When did the person stop working at this company?
  "#)
  years int
  description_of_work string @description(#"
    What work did the person do at this company?
    What responsibilites were handeled by the person at this company?
  "#)
}
class PersonalProjects {
  projects Project[] @description(#"
    List of personal projects the person has worked on. Usually under the Projects or Activites Header.
  "#)
}

class Project {
  name string @description(#"
    What is the name of the project?
  "#)
  technologies_used string[] @description(#"
    What technologies were used in this project?
  "#)
  description_of_work string[] @description(#"
    What does this project do?
  "#)
}

class Awards {
  awards Certificates[] @description(#"
    List of awards/certificates the person has received. Usually under the Awards Header.
  "#)
}

class Certificates {
  name string
  awarded_by string @description(#"
    Who awarded this award/certificate/course?
  "#)
}


// Create a function to extract the resume from a string.
function ExtractResume(resume: string, jobdescription: string) -> Resume {
  // Specify a client as provider/model-name
  // you can use custom LLM params with a custom client name from clients.baml like "client CustomHaiku"
  client Llama3 // Set OPENAI_API_KEY to use this client.
  prompt #"
    Given a resume
    {{ resume }}
    
    and a job description 
    {{ jobdescription }},

    Your task is to rewrite the given CV to fit the job description. Follow these guidelines:
     Be truthful and objective to the experience listed in the CV
     Rearrange projects and skills according to the requirement of the job
     Rewrite Job descriptions that match the job description but is also truthful
     Fix spelling and grammar errors
     Remove irrelevant information

    Extract from the updated CV. If no value is available for a field, provide an empty string:
    
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
