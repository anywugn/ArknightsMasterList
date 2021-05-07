import { useRequest } from "umi";

export interface IOperatorInfo {
  rare: number;
  class: string;
  name: string;
  filename: string;
}

export default function useOperatorList(): { operators: IOperatorInfo[], loading: boolean } {
  const { data, loading } = useRequest('/api/operators');

  return {
    operators: data,
    loading: loading,
  };
};
