import { useRequest } from "umi";

export interface ICostumeInfo {
  owner: string;
  series: string;
  name: string;
  code: number;
}

export default function useCostumeList(): { costumes: ICostumeInfo[], loading: boolean } {
  const { data, loading } = useRequest('/api/costumes');

  return {
    costumes: data,
    loading: loading,
  };
};
