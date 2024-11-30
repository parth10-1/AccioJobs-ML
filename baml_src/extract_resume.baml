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
  about_me string
}

class Contacts {
  name string
  title string
  email string
  phone string
  websiteURL string
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
  universities University[] 
}

class University {
  name string
  degree string
  major string
  score string
  startdate string
  enddate string
}

class Experience {
  companies Company[]
}

class Company {
  name string
  position string @description(#"
    What was the job title or position of the person at this company?
  "#)
  startdate string
  enddate string
  years int
  description_of_work string @description(#"
    What work did the person do at this company?
    What responsibilites were handeled by the person at this company?
  "#)
}
class PersonalProjects {
  projects Project[]
}

class Project {
  name string
  technologies_used string[]
  description_of_work string[] @description(#"
    What does this project do?
  "#)
}

class Awards {
  awards Certificates[]
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
    - Be truthful and objective to the experience listed in the CV
    - Rearrange projects and skills according to the requirement of the job
    - Be specific rather than general
    - Rewrite description of work items using STAR methodology (but do not mention STAR explicitly)
    - Fix spelling and grammar errors
    - Write to express not impress
    - Articulate and don't be flowery
    - Prefer active voice over passive voice
    
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
