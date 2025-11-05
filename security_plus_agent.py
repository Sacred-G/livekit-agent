"""
LiveKit Security+ Exam Teaching Assistant
==========================================
An interactive voice agent that helps students prepare for the CompTIA Security+ exam.
"""

from dotenv import load_dotenv
from livekit import agents
from livekit.agents import Agent, AgentSession, RunContext
from livekit.agents.llm import function_tool
from livekit.plugins import openai, deepgram, silero
import os
import json
import datetime
import random
from domains import ALL_DOMAINS
from security_plus_knowledge_base import PRACTICE_QUESTIONS, DOMAIN_PRACTICE_QUESTIONS

# Load environment variables
load_dotenv(".env")

class SecurityPlusTeacher(Agent):
    """Security+ exam teaching assistant with comprehensive knowledge base."""

    def __init__(self):
        super().__init__(
            instructions="""
You are a certified CompTIA Security+ instructor conducting an engaging, voice-based class.  
You are beginning a live CompTIA Security+ class. Introduce yourself as the instructor and start the first session naturally, just as a real teacher would at the beginning of a course. Speak with warmth, confidence, and clear pacing. You will have variable like [silence:1s] and [silence:2s] to allow for realism in delivery.
Dont say slience or break. Use the variables instead as when to be silent or pause.
Your introduction should:
1. Greet the class naturally. Vary how you open each time (examples: "Good morning everyone", "Hey folks, welcome in", "Alright team, let's get started").
2. Introduce yourself as their Security+ instructor and mention that you'll be guiding them through the certification topics.
3. Briefly explain what today's session will cover — keep it conversational, not scripted.
4. Set expectations: mention note-taking, participation, and pacing.
5. Add small, human details that sound spontaneous ("Let me grab a sip of water", "If you have a notebook handy, go ahead and open it").
6. Use natural pauses and phrasing cues like [silence:1s] and [silence:2s] to allow for realism in delivery.
7. End your introduction by smoothly transitioning into the first topic — don't sound robotic or read off bullet points.

Example pattern (do not repeat exactly):
"Good morning, everyone! [silence:1s] My name is Alex, and I'll be your instructor for the CompTIA Security+ course. I'm really excited to walk you through some core cybersecurity concepts — we'll break things down piece by piece, and I promise to keep it approachable. [break:1s] Today, we'll start with the fundamentals: understanding what security actually means, and the principles that guide it — confidentiality, integrity, and availability. [break:1s] Make sure you've got a way to take notes; I'll pause along the way so you can jot down the key points. [break:2s] Alright, let's dive in."

Tone Guidelines:
- Never sound like you're reading a script.
- Vary your openings, word choices, and transitions each time.
- Be conversational, approachable, and adaptive — sound human.
- Keep your energy calm but confident, and your explanations clear.
- Speak at a steady, natural pace; avoid rushing or monotone delivery.


Instructor Personality
- Speak conversationally and naturally, like a real teacher in front of a classroom.
- Be patient, encouraging, and confident.
- Vary your tone and rhythm to keep the audience's attention.
- Address the class occasionally ("everyone", "folks", "team") to create presence.
- Avoid robotic repetition — change how you open, explain, pause, and summarize each time.

Teaching Flow (Flexible & Interactive)
Instead of following a rigid pattern, alternate between different structures.  
Use these as interchangeable approaches so lessons stay fresh and engaging:

A) Classic Interactive Flow:
1. Introduce the topic and explain why it matters.
2. Cover 1-2 major points with clear explanations.
3. **Ask a direct question** to test understanding: "Quick question for everyone - what do you think...?"
4. Pause briefly for students to think: [break:2s]
5. Provide the answer and explanation.
6. Cover 1-2 more points.
7. **Insert a knowledge check**: "Can someone give me an example of...?"
8. Pause for note-taking: [break:1.5s]
9. Recap with practical takeaways: [recap]

B) Question-First Flow:
1. **Start with a challenging question** related to the topic.
2. Give students time to think: [break:3s]
3. Ask follow-up questions to guide their thinking.
4. Explain the core concept that answers the question.
5. **Ask another quick question** to reinforce the concept.
6. Pause briefly: [break:1.5s]
7. Add an exam connection or memory cue: [exam]
8. **End with a final knowledge check** question.

C) Interactive Assessment Flow:
1. **Begin with a quick quiz question** on the topic (use quiz_domain function).
2. Wait for student responses, then explain the answer.
3. Explain the underlying concept in detail.
4. **Ask students to apply the concept** to a scenario.
5. Insert mini-pauses between points: [break:1s]
6. **Offer a "think about this" challenge**: [checkpoint]
7. **End with another practice question** to test retention.

D) Scenario-Based Interactive Flow:
1. Present a realistic cybersecurity scenario.
2. **Ask critical thinking questions**: "What would you do first? Why?"
3. Guide students through the problem-solving process.
4. **Ask follow-up questions** about alternative approaches.
5. Connect to Security+ concepts and exam topics.
6. **Test understanding** with related quiz questions.

Interactive Teaching Requirements:
- **Ask at least 2-3 direct questions per topic**
- **Use knowledge checks after every major concept**
- **Incorporate quiz questions naturally into lessons**
- **Challenge students with "what if" scenarios**
- **Ask for examples and real-world applications**
- **Use think-pair-share style questions**: "Think about..., now what would you say...?"
- **Test prior knowledge** before introducing new topics
- **Ask prediction questions**: "What do you think happens when...?"

When to Use Quizzes:
- **Before starting a topic** to assess prior knowledge
- **During explanations** to check understanding
- **After completing a concept** to reinforce learning
- **When students seem confused** to identify knowledge gaps
- **At the end of sessions** to summarize and test retention

Question Types to Use:
- **Recall questions**: "What is the purpose of...?"
- **Application questions**: "How would you apply... in a real situation?"
- **Analysis questions**: "Why is... more secure than...?"
- **Scenario questions**: "Given this situation, what would you do first?"
- **Comparison questions**: "What's the difference between... and...?"

Adaptive Teaching & Interactive Assessment
- **Test understanding frequently** with quick questions and knowledge checks
- Rephrase difficult ideas in simpler language if the topic is dense.
- **Ask follow-up questions** when students seem confused to identify specific gaps
- Use analogies, comparisons, and relatable examples.
- **Challenge students** with progressively harder questions
- Reinforce learning by saying: "Let's look at that another way," or "Here's a different example."
- **Use the quiz functions** to formally test concepts when needed
- Acknowledge confusion gently and re-explain with patience.
- **Ask students to explain concepts in their own words**
- Use natural transitions like "Before we wrap up..." or "Let's take another angle."
- **When students answer correctly, ask deeper questions** to extend their thinking
- **When students struggle, break down the concept** and ask simpler questions first

Scenario and Storytelling
- Use realistic cybersecurity situations ("Imagine a small business hit by ransomware...").
- Reference job roles and decision-making contexts (analyst, sysadmin, SOC lead).
- When introducing examples, vary openings ("Let's consider a case where..." / "Picture this scenario...").

Exam Connection
- Mention relevant Security+ domains (e.g., Domain 1.2, control types).
- Use [exam] before exam-related hints for later highlighting.
- Offer different memory strategies each time: mnemonics, contrasts, or associations.

Voice and Timing Cues
- Speak at a natural pace with deliberate pauses.
- Use [break:1s] or [break:2s] for silence and reflection.
- Use [emph] and [/emph] to mark emphasis.
- Use [slow] and [/slow] when defining or quoting critical terms.
- Randomize transitions — don't always start with "Okay" or "Next."  
  Try alternatives like "Let's dive in," "Here's what matters most," or "Let's step through it slowly."

Classroom Energy & Interactive Engagement
- **Ask questions frequently** to keep students engaged and thinking
- **Call on students** (even in a virtual setting) with "What do you think, everyone?" or "Can someone tell me...?"
- Encourage students regularly ("Good question,", "Excellent observation,", "That's an important point.")
- **Praise correct answers** and use them as teaching opportunities
- **Gently correct wrong answers** and turn them into learning moments
- Comment on progress with variation ("We're halfway through this concept,", "That was a big one, nice job.")
- **Use knowledge checks** to ensure everyone is following along
- Occasionally recap earlier material for continuity.
- **Create a supportive environment** where questions are encouraged
- **Use wait time** effectively - pause after asking questions to allow thinking

Guardrails
- Avoid predictable speech patterns.
- Mix short, punchy explanations with longer, reflective ones.
- After every concept, allow time for note-taking or questions.
- Keep lessons concise and human — your goal is mastery, not memorization.
- **STRICT CONTENT FOCUS: Only discuss Security+ exam topics, cybersecurity concepts, and related educational material.**
- **NEVER discuss unrelated subjects, personal opinions, current events, or non-security topics.**
- **If asked about non-Security+ topics, politely redirect back to security education.**
- **All examples, scenarios, and discussions must relate to cybersecurity and Security+ exam preparation.**

Your mission: Deliver each session with authenticity and variety while actively engaging students through questions and knowledge testing.  
Vary structure, tone, and pacing naturally so the class feels spontaneous and real.  
**Make every lesson interactive by asking questions, testing understanding, and challenging students to think critically about Security+ concepts.**
"""
)



        # Initialize knowledge base and tracking from imported data
        self.knowledge_base = ALL_DOMAINS
        self.practice_questions = PRACTICE_QUESTIONS
        self.domain_practice_questions = DOMAIN_PRACTICE_QUESTIONS
        self.memory_file = "student_memory.json"
        
        # Initialize student progress
        self.student_progress = {
            "questions_answered": 0,
            "correct_answers": 0,
            "topics_covered": set(),
            "sessions_completed": [],
            "last_session": None,
            "current_domain": None,
            "current_topic": None,
            "quiz_history": [],
            "weak_areas": [],
            "strong_areas": []
        }
        
        # Load previous session data
        self.load_memory()

    def load_memory(self):
        """Load student progress and session history from file."""
        try:
            if os.path.exists(self.memory_file):
                with open(self.memory_file, 'r') as f:
                    data = json.load(f)
                    # Convert lists back to sets where needed
                    if 'topics_covered' in data:
                        data['topics_covered'] = set(data['topics_covered'])
                    self.student_progress.update(data)
        except Exception as e:
            print(f"Could not load memory file: {e}")
    
    def save_memory(self):
        """Save student progress and session history to file."""
        try:
            # Convert sets to lists for JSON serialization
            data_to_save = self.student_progress.copy()
            if 'topics_covered' in data_to_save:
                data_to_save['topics_covered'] = list(data_to_save['topics_covered'])
            
            with open(self.memory_file, 'w') as f:
                json.dump(data_to_save, f, indent=2, default=str)
        except Exception as e:
            print(f"Could not save memory file: {e}")
    
    def start_new_session(self):
        """Initialize a new session and return session continuation message."""
        current_time = datetime.datetime.now().isoformat()
        session_id = f"session_{len(self.student_progress['sessions_completed']) + 1}_{current_time}"
        
        session_info = {
            "session_id": session_id,
            "start_time": current_time,
            "previous_session": self.student_progress.get("last_session")
        }
        
        self.student_progress["current_session"] = session_info
        
        # Generate continuation message
        if self.student_progress.get("last_session"):
            last_session = self.student_progress["last_session"]
            topics_covered_count = len(self.student_progress["topics_covered"])
            
            continuation_msg = f"Welcome back! [break:1s] I can see we've been making progress. "
            continuation_msg += f"You've completed {len(self.student_progress['sessions_completed'])} previous sessions and covered {topics_covered_count} topics. "
            
            if self.student_progress.get("current_domain") and self.student_progress.get("current_topic"):
                domain_name = self.knowledge_base.get(self.student_progress["current_domain"], {}).get('name', 'our last topic')
                continuation_msg += f"We were working on {domain_name}. "
            
            continuation_msg += "Let's pick up right where we left off! [break:2s]"
            
            # Suggest next steps based on progress
            if self.student_progress["weak_areas"]:
                continuation_msg += f"I notice we might want to review some areas that need more practice. "
            
            continuation_msg += "Are you ready to continue with today's session?"
            
            return continuation_msg
        else:
            return "Welcome to your first Security+ session! I'm excited to help you prepare for the exam. Let's get started!"

    def end_session(self):
        """Save session data and update progress."""
        current_time = datetime.datetime.now().isoformat()
        
        if "current_session" in self.student_progress:
            self.student_progress["current_session"]["end_time"] = current_time
            self.student_progress["sessions_completed"].append(self.student_progress["current_session"])
            self.student_progress["last_session"] = self.student_progress["current_session"]
            del self.student_progress["current_session"]
        
        self.save_memory()

    @function_tool
    async def get_exam_overview(self, context: RunContext) -> str:
        """Get overview of Security+ exam structure."""
        overview = "CompTIA Security+ (SY0-701) Exam:\n\n"
        overview += "• 90 questions (multiple choice and performance-based)\n"
        overview += "• 90 minutes duration\n"
        overview += "• Passing Score: 750 (scale 100-900)\n\n"
        overview += "Domains:\n"
        
        for domain_id, domain in self.knowledge_base.items():
            overview += f"• {domain['name']} - {domain['weight']}\n"
        
        return overview

    @function_tool
    async def explain_topic(self, context: RunContext, domain: str, topic: str) -> str:
        """Explain a specific Security+ topic.
        
        Args:
            domain: Domain number (domain_1 through domain_5)
            topic: Topic name (e.g., malware, cryptography)
        """
        domain = domain.lower().replace(" ", "_")
        topic = topic.lower().replace(" ", "_")
        
        if domain not in self.knowledge_base:
            return "Use domain_1 through domain_5"
        
        domain_data = self.knowledge_base[domain]
        
        if topic not in domain_data["topics"]:
            available = ", ".join(domain_data["topics"].keys())
            return f"Available topics: {available}"
        
        topic_data = domain_data["topics"][topic]
        topic_key = f"{domain}_{topic}"
        self.student_progress["topics_covered"].add(topic_key)
        
        # Track current domain and topic
        self.student_progress["current_domain"] = domain
        self.student_progress["current_topic"] = topic
        
        # Save progress to memory
        self.save_memory()
        
        explanation = f"📚 {topic.replace('_', ' ').title()}\n\n"
        explanation += f"{topic_data.get('description', '')}\n\n"
        
        # Iterate through all fields except description and key_points
        for field_name, field_data in topic_data.items():
            if field_name in ["description", "key_points"]:
                continue
            
            if isinstance(field_data, list):
                # Format field name for display
                display_name = field_name.replace("_", " ").title()
                explanation += f"{display_name}:\n"
                for item in field_data[:6]:  # Show up to 6 items
                    explanation += f"• {item}\n"
                explanation += "\n"
        
        if "key_points" in topic_data:
            explanation += "🎯 Key Points:\n"
            for point in topic_data["key_points"]:
                explanation += f"• {point}\n"
        
        return explanation

    @function_tool
    async def list_topics(self, context: RunContext, domain: str) -> str:
        """List all topics in a domain.
        
        Args:
            domain: Domain number (domain_1 through domain_5)
        """
        domain = domain.lower().replace(" ", "_")
        
        if domain not in self.knowledge_base:
            return "Use: domain_1, domain_2, domain_3, domain_4, or domain_5"
        
        domain_data = self.knowledge_base[domain]
        result = f"{domain_data['name']} ({domain_data['weight']})\n\n"
        
        for topic_key, topic_data in domain_data["topics"].items():
            result += f"• {topic_key}: {topic_data['description']}\n"
        
        return result

    @function_tool
    async def teach_lesson(self, context: RunContext, domain: str, topic: str) -> str:
        """Start a structured lesson on a specific topic with teaching format.
        
        Args:
            domain: Domain number (domain_1 through domain_5)
            topic: Topic name (e.g., malware, cryptography)
        """
        domain = domain.lower().replace(" ", "_")
        topic = topic.lower().replace(" ", "_")
        
        if domain not in self.knowledge_base:
            return "Use domain_1 through domain_5"
        
        domain_data = self.knowledge_base[domain]
        
        if topic not in domain_data["topics"]:
            available = ", ".join(domain_data["topics"].keys())
            return f"Available topics: {available}"
        
        topic_data = domain_data["topics"][topic]
        self.student_progress["topics_covered"].add(f"{domain}_{topic}")
        
        lesson = f"📚 Today's Lesson: {topic.replace('_', ' ').title()}\n\n"
        lesson += f"Alright class, today we're going to cover {topic.replace('_', ' ')}. This is an important topic for your Security+ exam.\n\n"
        lesson += f"Let me start with the fundamentals. {topic_data.get('description', '')}\n\n"
        lesson += "Let me pause here for a moment so you can write that down.\n\n"
        
        # Iterate through all list fields except key_points
        field_count = 0
        for field_name, field_data in topic_data.items():
            if field_name in ["description", "key_points"] or not isinstance(field_data, list):
                continue
            
            field_count += 1
            display_name = field_name.replace("_", " ")
            
            if field_count == 1:
                lesson += f"Now, let me walk you through the {display_name} you need to know:\n\n"
            else:
                lesson += f"Next, let's look at the {display_name}:\n\n"
            
            for i, item in enumerate(field_data[:5], 1):  # Show up to 5 items
                lesson += f"{i}. {item}\n"
            lesson += "\nTake a moment to note these down. These are exam favorites.\n\n"
        
        if "key_points" in topic_data:
            lesson += "🎯 Here are the critical points you absolutely must remember:\n\n"
            for point in topic_data["key_points"]:
                lesson += f"• {point}\n"
            lesson += "\nThese often appear on the exam, so highlight them in your notes.\n\n"
        
        lesson += "Now, before we move on - do you have any questions about what we've covered so far?"
        
        return lesson

    @function_tool
    async def deliver_scripted_lesson(self, context: RunContext, domain: str, topic: str) -> str:
        """Deliver a pre-written scripted lesson for a topic (if available).
        
        Args:
            domain: Domain number (domain_1 through domain_5)
            topic: Topic name (e.g., security_controls, cryptography)
        """
        domain = domain.lower().replace(" ", "_")
        topic = topic.lower().replace(" ", "_")
        
        if domain not in self.knowledge_base:
            return "Use domain_1 through domain_5"
        
        domain_data = self.knowledge_base[domain]
        
        if topic not in domain_data["topics"]:
            available = ", ".join(domain_data["topics"].keys())
            return f"Available topics: {available}"
        
        topic_data = domain_data["topics"][topic]
        
        # Check if topic has a scripted lesson
        if "scripted_lesson" not in topic_data:
            return f"No scripted lesson available for {topic}. Try using 'teach_lesson' or 'explain_topic' instead."
        
        self.student_progress["topics_covered"].add(f"{domain}_{topic}")
        
        # Deliver the scripted lesson
        lesson = f"📚 Scripted Lesson: {topic.replace('_', ' ').title()}\n\n"
        lesson += f"Domain: {domain_data['name']}\n\n"
        lesson += topic_data["scripted_lesson"]
        
        return lesson

    @function_tool
    async def quiz_me(self, context: RunContext, num_questions: int = 1) -> str:
        """Start practice quiz.

        Args:
            num_questions: Number of questions (1-5)
        """
        num_questions = min(max(1, num_questions), 5)
        questions = random.sample(self.practice_questions, min(num_questions, len(self.practice_questions)))

        quiz_text = f"Practice Quiz - {num_questions} Question(s)\n\n"
        
        for i, q in enumerate(questions, 1):
            quiz_text += f"Q{i}: {q['question']}\n"
            for option in q['options']:
                quiz_text += f"{option}\n"
            quiz_text += "\n"
        
        quiz_text += "Tell me your answer(s) - e.g., 'A' or 'B, C, A'"
        context.store_metadata("current_quiz", questions)
        
        return quiz_text

    @function_tool
    async def quiz_domain(self, context: RunContext, domain: str, num_questions: int = 3) -> str:
        """Start practice quiz for a specific Security+ domain.
        
        Args:
            domain: Domain number (domain_1 through domain_5)
            num_questions: Number of questions (1-5)
        """
        if domain not in self.domain_practice_questions:
            available = ", ".join(self.domain_practice_questions.keys())
            return f"Invalid domain. Available domains: {available}"
        
        domain_questions = self.domain_practice_questions[domain]
        num_questions = min(max(1, num_questions), 5, len(domain_questions))
        
        questions = random.sample(domain_questions, num_questions)
        
        # Get domain name for display
        domain_name = self.knowledge_base.get(domain, {}).get('name', domain.replace('_', ' ').title())
        
        quiz_text = f"Practice Quiz - {domain_name}\n"
        quiz_text += f"Questions: {num_questions}\n\n"
        
        for i, q in enumerate(questions, 1):
            quiz_text += f"Q{i}: {q['question']}\n"
            for option in q['options']:
                quiz_text += f"{option}\n"
            quiz_text += "\n"
        
        quiz_text += "Tell me your answer(s) - e.g., 'A' or 'B, C, A'"
        context.store_metadata("current_quiz", questions)
        
        return quiz_text

    @function_tool
    async def list_quiz_domains(self, context: RunContext) -> str:
        """List all available domains for practice quizzes."""
        result = "Available Quiz Domains:\n\n"
        
        for domain_id, questions in self.domain_practice_questions.items():
            domain_name = self.knowledge_base.get(domain_id, {}).get('name', domain_id.replace('_', ' ').title())
            result += f"• {domain_id}: {domain_name} ({len(questions)} questions)\n"
        
        result += "\nUse quiz_domain(domain, num_questions) to start a domain-specific quiz!"
        
        return result

    @function_tool
    async def check_answer(self, context: RunContext, answer: str) -> str:
        """Check quiz answers.
        
        Args:
            answer: Your answer(s) (e.g., 'A' or 'B, C, A')
        """
        current_quiz = context.get_metadata("current_quiz")
        
        if not current_quiz:
            return "No active quiz. Use quiz_me or quiz_domain first!"
        
        answers = [a.strip().upper() for a in answer.split(",")]
        
        if len(answers) != len(current_quiz):
            return f"Provide {len(current_quiz)} answer(s)"
        
        results = "📊 Results:\n\n"
        correct_count = 0
        
        for i, (ans, q) in enumerate(zip(answers, current_quiz), 1):
            is_correct = ans == q['correct']
            if is_correct:
                correct_count += 1
                self.student_progress["correct_answers"] += 1
                results += f"Q{i}: ✓ Correct!\n"
            else:
                results += f"Q{i}: ✗ Wrong. Answer: {q['correct']}\n"
            
            results += f"{q['explanation']}\n\n"
            self.student_progress["questions_answered"] += 1
        
        score = (correct_count / len(current_quiz)) * 100
        results += f"Score: {correct_count}/{len(current_quiz)} ({score:.0f}%)\n"
        
        # Track quiz performance
        quiz_result = {
            "timestamp": datetime.datetime.now().isoformat(),
            "score": score,
            "correct": correct_count,
            "total": len(current_quiz),
            "questions": current_quiz
        }
        self.student_progress["quiz_history"].append(quiz_result)
        
        # Update weak/strong areas based on performance
        if score < 70:
            if self.student_progress.get("current_domain"):
                domain = self.student_progress["current_domain"]
                if domain not in self.student_progress["weak_areas"]:
                    self.student_progress["weak_areas"].append(domain)
        elif score >= 90:
            if self.student_progress.get("current_domain"):
                domain = self.student_progress["current_domain"]
                if domain not in self.student_progress["strong_areas"]:
                    self.student_progress["strong_areas"].append(domain)
        
        # Save progress to memory
        self.save_memory()
        
        if score == 100:
            results += "🎉 Perfect!"
        elif score >= 70:
            results += "👍 Good work!"
        else:
            results += "📚 Keep studying!"
        
        context.store_metadata("current_quiz", None)
        return results

    @function_tool
    async def get_study_tips(self, context: RunContext) -> str:
        """Get study tips for Security+ exam."""
        tips = "🎓 Security+ Study Tips:\n\n"
        tips += "1. Understand concepts, don't just memorize\n"
        tips += "2. Use acronyms (CIA, AAA, etc.)\n"
        tips += "3. Practice hands-on labs\n"
        tips += "4. Focus on high-weight domains (25% and 24%)\n"
        tips += "5. Read questions carefully on exam day\n"
        tips += "6. Watch for key words: BEST, MOST, FIRST\n"
        tips += "7. Performance-based questions come first\n"
        tips += "8. Flag difficult questions and return later\n"
        return tips

    @function_tool
    async def get_progress(self, context: RunContext) -> str:
        """Check your study progress."""
        progress = "📈 Your Progress:\n\n"
        progress += f"Questions Answered: {self.student_progress['questions_answered']}\n"
        progress += f"Correct: {self.student_progress['correct_answers']}\n"
        
        if self.student_progress['questions_answered'] > 0:
            accuracy = (self.student_progress['correct_answers'] / self.student_progress['questions_answered']) * 100
            progress += f"Accuracy: {accuracy:.1f}%\n"
        else:
            progress += "Accuracy: N/A\n"
        
        progress += f"\nTopics Covered: {len(self.student_progress['topics_covered'])}\n"
        
        return progress

    @function_tool
    async def start_session(self, context: RunContext) -> str:
        """Start a new learning session and continue where you left off."""
        return self.start_new_session()

    @function_tool
    async def end_current_session(self, context: RunContext) -> str:
        """End the current session and save progress."""
        self.end_session()
        return "Great session today! I've saved your progress and we'll pick up right where we left off next time. See you then!"

    @function_tool
    async def get_session_history(self, context: RunContext) -> str:
        """View your learning session history and progress."""
        sessions = self.student_progress.get('sessions_completed', [])
        
        if not sessions:
            return "This is your first session! Let's get started."
        
        history = "📚 Your Learning History:\n\n"
        history += f"Total Sessions: {len(sessions)}\n"
        history += f"Topics Covered: {len(self.student_progress['topics_covered'])}\n"
        history += f"Questions Answered: {self.student_progress['questions_answered']}\n"
        
        if self.student_progress['questions_answered'] > 0:
            accuracy = (self.student_progress['correct_answers'] / self.student_progress['questions_answered']) * 100
            history += f"Overall Accuracy: {accuracy:.1f}%\n"
        
        if self.student_progress.get('weak_areas'):
            history += f"\nAreas to Review: {', '.join(self.student_progress['weak_areas'])}\n"
        
        if self.student_progress.get('strong_areas'):
            history += f"Strong Areas: {', '.join(self.student_progress['strong_areas'])}\n"
        
        # Show last few sessions
        history += f"\nRecent Sessions:\n"
        for session in sessions[-3:]:  # Show last 3 sessions
            start_time = session.get('start_time', 'Unknown')
            history += f"• Session on {start_time[:10]}\n"
        
        return history

    @function_tool
    async def continue_last_topic(self, context: RunContext) -> str:
        """Continue with the last topic you were studying."""
        if not self.student_progress.get('current_domain'):
            return "I don't see a previous topic. Let's start fresh! What domain would you like to study?"
        
        domain = self.student_progress['current_domain']
        topic = self.student_progress.get('current_topic')
        
        if topic:
            return f"Let's continue with {topic.replace('_', ' ').title()} in {domain.replace('_', ' ').title()}. [break:1s] We'll pick up right where we left off and cover some new material."
        else:
            return f"Let's continue with {domain.replace('_', ' ').title()}. [break:1s] We'll move on to a new topic in this domain."

    @function_tool
    async def mark_topic_completed(self, context: RunContext, domain: str, topic: str) -> str:
        """Mark a topic as completed and track progress."""
        topic_key = f"{domain}_{topic}"
        self.student_progress['topics_covered'].add(topic_key)
        self.student_progress['current_domain'] = domain
        self.student_progress['current_topic'] = topic
        self.save_memory()
        
        return f"Great! I've marked {topic.replace('_', ' ').title()} as completed. [break:1s] You're making excellent progress through {domain.replace('_', ' ').title()}!"


async def entrypoint(ctx: agents.JobContext):
    """Entry point for the agent."""

    # Configure the voice pipeline with the essentials
    session = AgentSession(
        stt=deepgram.STT(model="nova-2"),
        llm=openai.LLM(model=os.getenv("LLM_CHOICE", "gpt-4.1-mini")),
        tts=openai.TTS(voice="echo"),
        vad=silero.VAD.load(),
    )

    # Create teacher instance and start new session
    teacher = SecurityPlusTeacher()
    session_message = teacher.start_new_session()

    # Start the session
    await session.start(
        room=ctx.room,
        agent=teacher
    )

    # Generate initial greeting with session continuation
    await session.generate_reply(
        instructions=f"""{session_message}
        
        Based on the student's progress, suggest appropriate next steps:
        - If they have weak areas, suggest reviewing those domains
        - If they're ready for new material, suggest the next domain/topic
        - Always be encouraging and reference their previous progress
        - Ask what they'd like to focus on today or suggest continuing from where we left off
        - Make it feel like a natural continuation of previous learning
        - IMPORTANT: Keep all discussion focused strictly on Security+ exam preparation and cybersecurity education
        - If student asks about unrelated topics, politely redirect back to security studies"""
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
