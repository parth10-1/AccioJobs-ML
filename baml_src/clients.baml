
client<llm> Llama3_2 {
  provider ollama
  retry_policy Constant
  options {
    base_url "https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-3B-Instruct/v1/"
    model "meta-llama/Llama-3.2-3B-Instruct"
    api_key env.API_KEY
    timeout_ms 60000
    request_timeout_ms 30000
    max_tokens 2000
  }
}

// https://docs.boundaryml.com/docs/snippets/clients/retry
retry_policy Constant {
  max_retries 3
  // Strategy is optional
  strategy {
    type constant_delay
    delay_ms 200
  }
}
