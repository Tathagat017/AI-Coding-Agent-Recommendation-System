import { useState } from "react";
import {
  MantineProvider,
  Container,
  Title,
  Text,
  Paper,
  Group,
  Stack,
  Button,
  Textarea,
  Card,
  Badge,
  Loader,
  Center,
  ThemeIcon,
} from "@mantine/core";
import {
  IconBrain,
  IconSearch,
  IconStar,
  IconCheck,
} from "@tabler/icons-react";

interface Agent {
  name: string;
  score: number;
  justification: string;
  strengths: string[];
  use_cases: string[];
  pricing: string;
  tools: string[];
}

interface Recommendation {
  recommendations: Agent[];
  task_analysis: {
    complexity: string;
    project_type: string;
    workflow: string;
    experience_level: string;
  };
}

function App() {
  const [task, setTask] = useState("");
  const [recommendations, setRecommendations] = useState<Recommendation | null>(
    null
  );
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!task.trim()) return;

    setLoading(true);
    try {
      const response = await fetch("http://localhost:8000/recommend", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ description: task }),
      });

      if (response.ok) {
        const data = await response.json();
        setRecommendations(data);
      } else {
        console.error("Failed to get recommendations");
      }
    } catch (error) {
      console.error("Error:", error);
    } finally {
      setLoading(false);
    }
  };

  const getAgentColor = (index: number) => {
    const colors = ["blue", "green", "orange"];
    return colors[index] || "gray";
  };

  const exampleTasks = [
    "Build a React e-commerce website with payment integration",
    "Create a machine learning model for image classification",
    "Develop a REST API with authentication and database",
    "Fix bugs in existing Python Django application",
  ];

  return (
    <MantineProvider>
      <Container size="lg" py="xl">
        <Stack gap="xl">
          {/* Header */}
          <Paper
            p="xl"
            radius="md"
            withBorder
            style={{
              background: "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
            }}
          >
            <Group gap="md" align="center">
              <ThemeIcon size={60} radius="md" color="white" variant="light">
                <IconBrain size={30} />
              </ThemeIcon>
              <div>
                <Title order={1} c="white" size="h1">
                  AI Coding Agent Recommender
                </Title>
                <Text size="lg" c="white" opacity={0.9} mt="xs">
                  Find the perfect AI coding assistant for your project
                </Text>
              </div>
            </Group>
          </Paper>

          {/* Features */}
          <Group grow>
            <Card shadow="sm" padding="lg" radius="md" withBorder>
              <Center>
                <ThemeIcon size={50} radius="md" color="blue">
                  <IconSearch size={25} />
                </ThemeIcon>
              </Center>
              <Text ta="center" fw={500} mt="md">
                Smart Analysis
              </Text>
              <Text size="sm" c="dimmed" ta="center" mt="xs">
                Our AI analyzes your task complexity, type, and requirements
              </Text>
            </Card>

            <Card shadow="sm" padding="lg" radius="md" withBorder>
              <Center>
                <ThemeIcon size={50} radius="md" color="green">
                  <IconStar size={25} />
                </ThemeIcon>
              </Center>
              <Text ta="center" fw={500} mt="md">
                Top 3 Matches
              </Text>
              <Text size="sm" c="dimmed" ta="center" mt="xs">
                Get ranked recommendations with detailed justifications
              </Text>
            </Card>

            <Card shadow="sm" padding="lg" radius="md" withBorder>
              <Center>
                <ThemeIcon size={50} radius="md" color="orange">
                  <IconCheck size={25} />
                </ThemeIcon>
              </Center>
              <Text ta="center" fw={500} mt="md">
                Expert Insights
              </Text>
              <Text size="sm" c="dimmed" ta="center" mt="xs">
                Learn about strengths, tools, and pricing for each agent
              </Text>
            </Card>
          </Group>

          {/* Task Input */}
          <Paper p="xl" radius="md" withBorder>
            <form onSubmit={handleSubmit}>
              <Stack gap="md">
                <Title order={2} ta="center">
                  Describe Your Coding Task
                </Title>
                <Text ta="center" c="dimmed">
                  Get personalized recommendations from our intelligent system
                  that analyzes GitHub Copilot, Cursor, and Replit.
                </Text>

                <Textarea
                  placeholder="Describe your coding task..."
                  value={task}
                  onChange={(e) => setTask(e.target.value)}
                  minRows={4}
                  size="lg"
                  radius="md"
                />

                <Button
                  type="submit"
                  loading={loading}
                  size="lg"
                  radius="md"
                  fullWidth
                >
                  Get AI Recommendations
                </Button>

                <div>
                  <Text size="sm" fw={500} mb="xs">
                    Try these examples:
                  </Text>
                  <Group gap="xs">
                    {exampleTasks.map((example, index) => (
                      <Button
                        key={index}
                        variant="light"
                        size="xs"
                        radius="xl"
                        onClick={() => setTask(example)}
                      >
                        {example}
                      </Button>
                    ))}
                  </Group>
                </div>
              </Stack>
            </form>
          </Paper>

          {/* Loading */}
          {loading && (
            <Center>
              <Stack align="center" gap="md">
                <Loader size="lg" />
                <Text>
                  Analyzing your task and finding the best AI coding agents...
                </Text>
              </Stack>
            </Center>
          )}

          {/* Results */}
          {recommendations && !loading && (
            <Stack gap="xl">
              {/* Task Analysis */}
              <Paper p="lg" radius="md" withBorder>
                <Title order={3} mb="md">
                  Task Analysis
                </Title>
                <Group gap="xl">
                  <div>
                    <Text fw={500}>Complexity:</Text>
                    <Badge size="lg" variant="light" color="blue">
                      {recommendations.task_analysis.complexity}
                    </Badge>
                  </div>
                  <div>
                    <Text fw={500}>Type:</Text>
                    <Badge size="lg" variant="light" color="green">
                      {recommendations.task_analysis.project_type}
                    </Badge>
                  </div>
                  <div>
                    <Text fw={500}>Workflow:</Text>
                    <Badge size="lg" variant="light" color="purple">
                      {recommendations.task_analysis.workflow}
                    </Badge>
                  </div>
                </Group>
              </Paper>

              {/* Recommendations */}
              <Title order={2} ta="center">
                Recommended AI Coding Agents
              </Title>
              <Stack gap="lg">
                {recommendations.recommendations.map((agent, index) => (
                  <Card
                    key={agent.name}
                    shadow="lg"
                    padding="xl"
                    radius="md"
                    withBorder
                  >
                    <Group justify="space-between" mb="md">
                      <Group gap="md">
                        <Badge
                          size="xl"
                          variant="filled"
                          color={getAgentColor(index)}
                        >
                          #{index + 1}
                        </Badge>
                        <Title order={3}>{agent.name}</Title>
                      </Group>
                      <Badge
                        size="lg"
                        variant="light"
                        color={getAgentColor(index)}
                      >
                        Score: {agent.score}/100
                      </Badge>
                    </Group>

                    <Text mb="md" c="dimmed">
                      {agent.justification}
                    </Text>

                    <Group grow align="flex-start">
                      <div>
                        <Text fw={500} mb="xs">
                          Strengths:
                        </Text>
                        <Stack gap="xs">
                          {agent.strengths.map((strength, idx) => (
                            <Group key={idx} gap="xs">
                              <IconCheck size={16} color="green" />
                              <Text size="sm">{strength}</Text>
                            </Group>
                          ))}
                        </Stack>
                      </div>

                      <div>
                        <Text fw={500} mb="xs">
                          Best For:
                        </Text>
                        <Stack gap="xs">
                          {agent.use_cases.map((use, idx) => (
                            <Badge key={idx} variant="outline" size="sm">
                              {use}
                            </Badge>
                          ))}
                        </Stack>
                      </div>

                      <div>
                        <Text fw={500} mb="xs">
                          Pricing:
                        </Text>
                        <Text size="sm" c="blue" fw={500}>
                          {agent.pricing}
                        </Text>
                      </div>
                    </Group>
                  </Card>
                ))}
              </Stack>
            </Stack>
          )}
        </Stack>
      </Container>
    </MantineProvider>
  );
}

export default App;
