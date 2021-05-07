import OperatorSelector from '@/components/OperatorSelector';
import styles from './index.less';
import { InputNumber, Divider, Space, Select } from "antd";
import { useState } from 'react';
import CostumeSelector from '@/components/CostumeSelector';

export default function IndexPage() {
  const [skillNum, setSkillNum] = useState(0);

  const [ potential, setPotential ] = useState(1);
  const [ charLevel, setCharLevel ] = useState(10);

  const [ charName, setCharName ] = useState('');

  const skillStates = Array(3).fill(0).map(() => useState(0));

  const flushStates = () => {
    setPotential(1);
    setCharLevel(10);

    skillStates.map(([_, setSkillLevel]) => {
      setSkillLevel(0);
    })
  };

  return (
    <div>
      <h1 className={styles.title}>Page index</h1>

      <Divider />
      <Space>
        <OperatorSelector setSkillNum={setSkillNum} flushSkills={flushStates} setCharName={setCharName} />
        <CostumeSelector charName={charName} />
      </Space>

      <Divider />
      <Space>
        潜能
        <InputNumber
          min={1}
          max={6}
          value={potential}
          onChange={setPotential}
        />
        <Divider type='vertical' />
        等级
        <InputNumber
          min={10}
          max={90}
          step={10}
          value={charLevel}
          onChange={setCharLevel}
        />
      </Space>

      <Divider />
      {
        skillStates.map(([skillLevel, setSkillLevel], i) => (<Space>
          {`技能${i}`}
          <InputNumber
            min={0}
            max={3}
            value={skillLevel}
            onChange={setSkillLevel}
            disabled={skillNum < i + 1}
          />
          <Divider type='vertical' />
        </Space>))
      }
    </div>
  );
}
