import Browserbase from "@browserbasehq/sdk";
import "dotenv/config";

async function researchRagAlternatives() {
    const bb = new Browserbase({ apiKey: process.env.BROWSERBASE_API_KEY });

    console.log("🔍 Searching for open-source, self-hosted RAG alternatives to Dify with strong Google integration...");
    
    const query = "best self-hosted open source RAG system alternative to dify.ai with google drive and google search integration local api";
    
    try {
        const searchResponse = await bb.search.web({ 
            query: query, 
            numResults: 10 
        });

        console.log("\n--- Top Search Results ---");
        for (const result of searchResponse.results) {
            console.log(`\nTitle: ${result.title}\nURL: ${result.url}\nSnippet: ${result.snippet}`);
        }

        // Based on typical high-quality results, we'll want to deep dive into a few specific candidates
        // common ones: AnythingLLM, Flowise, LangFlow, Verba
        const candidates = ["AnythingLLM", "FlowiseAI", "LangFlow", "Verba"];
        
        for (const candidate of candidates) {
            console.log(`\n--- Deep Diving into ${candidate} ---`);
            const candidateSearch = await bb.search.web({ 
                query: `${candidate} self-hosted google integration local api RAG`, 
                numResults: 3 
            });
            
            for (const res of candidateSearch.results) {
                console.log(`- ${res.title}: ${res.url}`);
            }
        }

    } catch (error) {
        console.error("Research error:", error);
    }
}

researchRagAlternatives();
